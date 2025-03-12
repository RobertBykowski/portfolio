from flask import Flask, jsonify, request, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, fields
from sqlalchemy import or_, and_
import logging

app = Flask(__name__)

# Konfiguracja logowania
logging.basicConfig(level=logging.DEBUG)

# Konfiguracja bazy danych SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'twoj_tajny_klucz'  # Wymagane dla flash messages
db = SQLAlchemy(app)

# Inicjalizacja Swaggera
api = Api(app, doc='/swagger', title='System zarządzania produktami', 
         description='API do zarządzania produktami')

# Model bazy danych (tabela items)
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)  # Przechowujemy kwotę w groszach

    @property
    def formatted_price(self):
        return self.price / 100.0

    @formatted_price.setter
    def formatted_price(self, value):
        if value <= 0 or value > 900000.00:
            raise ValueError("Cena musi być większa od 0 i nie większa niż 900000.00 PLN")
        self.price = int(value * 100)

# Tworzenie bazy danych
with app.app_context():
    db.create_all()

# Model danych dla Swaggera
item_model = api.model('Item', {
    'id': fields.Integer(readOnly=True, description='Unikalny identyfikator produktu'),
    'name': fields.String(required=True, description='Nazwa produktu'),
    'price': fields.Float(required=True, description='Cena produktu w PLN')
})

item_create_model = api.model('ItemCreate', {
    'name': fields.String(required=True, description='Nazwa produktu'),
    'price': fields.Float(required=True, description='Cena produktu w PLN')
})

# Model parametrów filtrowania dla Swaggera
filter_parser = api.parser()
filter_parser.add_argument('nazwa', type=str, help='Filtruj po nazwie (częściowe dopasowanie)')
filter_parser.add_argument('cena_od', type=float, help='Minimalna cena w PLN')
filter_parser.add_argument('cena_do', type=float, help='Maksymalna cena w PLN')
filter_parser.add_argument('page', type=int, help='Numer strony (domyślnie 1)', default=1)
filter_parser.add_argument('per_page', type=int, help='Liczba elementów na stronę (domyślnie 10)', default=10)

@api.route('/items')
class ItemList(Resource):
    @api.doc('list_items')
    @api.expect(filter_parser)
    @api.marshal_with(item_model)
    def get(self):
        """Lista wszystkich produktów z możliwością filtrowania"""
        # Pobierz parametry filtrowania
        args = filter_parser.parse_args()
        nazwa = args.get('nazwa')
        cena_od = args.get('cena_od')
        cena_do = args.get('cena_do')
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        # Walidacja parametrów paginacji
        if page < 1:
            page = 1
        if per_page < 1 or per_page > 100:
            per_page = 10

        # Rozpocznij budowanie zapytania
        query = Item.query

        # Zastosuj filtry
        filters = []
        if nazwa:
            filters.append(Item.name.ilike(f'%{nazwa}%'))
        if cena_od is not None:
            filters.append(Item.price >= int(cena_od * 100))
        if cena_do is not None:
            filters.append(Item.price <= int(cena_do * 100))

        if filters:
            query = query.filter(and_(*filters))

        # Zastosuj paginację
        total = query.count()
        items = query.offset((page - 1) * per_page).limit(per_page).all()

        # Dodaj nagłówki paginacji do odpowiedzi
        response = [{'id': item.id, 'name': item.name, 'price': item.formatted_price} for item in items]
        
        # Dodaj metadane paginacji do odpowiedzi API
        pagination = {
            'total': total,
            'page': page,
            'per_page': per_page,
            'pages': (total + per_page - 1) // per_page
        }
        
        return response

    @api.doc('create_item')
    @api.expect(item_create_model)
    @api.marshal_with(item_model, code=201)
    def post(self):
        """Dodaj nowy produkt"""
        data = api.payload
        if data['price'] <= 0:
            api.abort(400, "Cena musi być większa od 0")
        new_item = Item(name=data['name'])
        new_item.formatted_price = data['price']
        db.session.add(new_item)
        db.session.commit()
        return {
            'id': new_item.id, 'name': new_item.name, 'price': new_item.formatted_price
        }, 201

@api.route('/items/<int:item_id>')
@api.param('item_id', 'Identyfikator produktu')
class ItemResource(Resource):
    @api.doc('get_item')
    @api.marshal_with(item_model)
    def get(self, item_id):
        """Pobierz produkt po ID"""
        item = Item.query.get_or_404(item_id)
        return {'id': item.id, 'name': item.name, 'price': item.formatted_price}

    @api.doc('delete_item')
    @api.response(204, 'Produkt usunięty')
    def delete(self, item_id):
        """Usuń produkt po ID"""
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return '', 204

    @api.doc('update_item')
    @api.expect(item_create_model)
    @api.marshal_with(item_model)
    def put(self, item_id):
        """Zaktualizuj produkt po ID"""
        data = api.payload
        if data['price'] <= 0:
            api.abort(400, "Cena musi być większa od 0")
        item = Item.query.get_or_404(item_id)
        item.name = data['name']
        item.formatted_price = data['price']
        db.session.commit()
        return {'id': item.id, 'name': item.name, 'price': item.formatted_price}

# Endpointy front-end
@app.route('/items-list')
def items_list():
    try:
        # Pobierz parametry filtrowania z query string
        nazwa = request.args.get('nazwa', '').strip()
        cena_od = request.args.get('cena_od', type=float)
        cena_do = request.args.get('cena_do', type=float)
        page = request.args.get('page', 1, type=int)
        per_page = 10  # Stała liczba elementów na stronę dla widoku HTML

        app.logger.debug('Parametry filtrowania: nazwa=%s, cena_od=%s, cena_do=%s, page=%s', 
                        nazwa, cena_od, cena_do, page)

        # Walidacja parametrów paginacji
        if page < 1:
            page = 1

        # Rozpocznij budowanie zapytania
        query = Item.query

        # Zastosuj filtry
        filters = []
        if nazwa:
            filters.append(Item.name.ilike(f'%{nazwa}%'))
        if cena_od is not None:
            filters.append(Item.price >= int(cena_od * 100))
        if cena_do is not None:
            filters.append(Item.price <= int(cena_do * 100))

        if filters:
            query = query.filter(and_(*filters))

        # Zastosuj paginację
        total = query.count()
        items = query.offset((page - 1) * per_page).limit(per_page).all()

        app.logger.debug('Znaleziono %d produktów', total)

        # Przygotuj dane paginacji
        pagination = {
            'total': total,
            'page': page,
            'per_page': per_page,
            'pages': (total + per_page - 1) // per_page
        }

        return render_template('items.html', 
                             items=items, 
                             pagination=pagination,
                             max=max,  # Dodajemy funkcję max do kontekstu
                             min=min)  # Dodajemy funkcję min do kontekstu
    except Exception as e:
        app.logger.error('Błąd podczas wyświetlania listy produktów: %s', str(e), exc_info=True)
        return render_template('500.html'), 500

@app.route('/create-item', methods=['POST', 'GET'])
def create_item_form():
    if request.method == 'POST':
        try:
            name = request.form['name']
            price = float(request.form['price'])
            if price <= 0:
                flash("Cena musi być większa od 0", "error")
                return redirect(url_for('create_item_form'))
            new_item = Item(name=name)
            new_item.formatted_price = price
            db.session.add(new_item)
            db.session.commit()
            flash("Produkt został pomyślnie dodany!", "success")
            return redirect(url_for('items_list'))
        except ValueError as e:
            flash(str(e), "error")
            return redirect(url_for('create_item_form'))
    return render_template('add_item.html')

@app.route('/update-item/<int:item_id>', methods=['POST', 'GET'])
def update_item_form(item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == 'POST':
        try:
            name = request.form['name']
            price = float(request.form['price'])
            if price <= 0:
                flash("Cena musi być większa od 0", "error")
                return redirect(url_for('update_item_form', item_id=item_id))
            item.name = name
            item.formatted_price = price
            db.session.commit()
            flash("Produkt został pomyślnie zaktualizowany!", "success")
            return redirect(url_for('items_list'))
        except ValueError as e:
            flash(str(e), "error")
            return redirect(url_for('update_item_form', item_id=item_id))
    return render_template('update_item.html', item=item)

@app.route('/delete-item/<int:item_id>')
def delete_item_form(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash("Produkt został pomyślnie usunięty!", "success")
    return redirect(url_for('items_list'))

@app.route('/')
def home():
    return redirect(url_for('items_list'))

# Obsługa błędów
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500_error(e):
    app.logger.error('Wystąpił błąd 500: %s', str(e))
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# http://127.0.0.1:5000/swagger
# http://127.0.0.1:5000/items-list