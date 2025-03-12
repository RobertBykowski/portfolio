from app3 import app, db, Item

# Lista przykładowych produktów (nazwa, cena w PLN)
sample_products = [
    ("Laptop Dell XPS 13", 5999.99),
    ("Smartfon Samsung Galaxy S21", 3499.99),
    ("Słuchawki Sony WH-1000XM4", 1299.99),
    ("Tablet iPad Air", 2799.99),
    ("Klawiatura mechaniczna", 449.99),
    ("Mysz bezprzewodowa", 199.99),
    ("Monitor 27\" 4K", 1899.99),
    ("Dysk SSD 1TB", 499.99),
    ("Kamera internetowa HD", 299.99),
    ("Powerbank 20000mAh", 159.99),
    ("Głośnik Bluetooth", 399.99),
    ("Drukarka laserowa", 899.99),
    ("Router Wi-Fi 6", 699.99),
    ("Pendrive 128GB", 89.99),
    ("Kabel HDMI 2m", 49.99),
    ("Ładowarka USB-C", 79.99),
    ("Podkładka pod mysz", 39.99),
    ("Torba na laptopa", 149.99),
    ("Stacja dokująca", 599.99),
    ("Kamera sportowa", 899.99)
]

def add_sample_data():
    with app.app_context():
        # Usuń istniejące produkty
        Item.query.delete()
        
        # Dodaj nowe produkty
        for name, price in sample_products:
            item = Item(name=name)
            item.formatted_price = price
            db.session.add(item)
        
        # Zapisz zmiany w bazie
        db.session.commit()
        print(f"Dodano {len(sample_products)} przykładowych produktów do bazy danych.")

if __name__ == "__main__":
    add_sample_data() 