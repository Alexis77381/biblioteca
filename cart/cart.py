from decimal import Decimal
from catalog.models import Book

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if not cart:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, book, quantity=1):
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0, 'price': str(book.price)}
        self.cart[book_id]['quantity'] += quantity
        self.session.modified = True

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        cart = self.cart.copy()
        
        for book in books:
            cart[str(book.id)]['book'] = book

        for item in cart.values():
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())