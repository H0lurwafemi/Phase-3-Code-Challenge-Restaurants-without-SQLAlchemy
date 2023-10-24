class Customer:
    _all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []
        Customer._all_customers.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls._all_customers

    def restaurants(self):
        return list({review.restaurant() for review in self._reviews})

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)

    def num_reviews(self):
        return len(self._reviews)

    @classmethod
    def find_by_name(cls, name):
        return next(
            (
                customer
                for customer in cls._all_customers
                if customer.full_name() == name
            ),
            None,
        )

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [
            customer
            for customer in cls._all_customers
            if customer.given_name() == given_name
        ]


class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews = []

    def name(self):
        return self._name

    def reviews(self):
        return self._reviews

    def average_star_rating(self):
        if not self._reviews:
            return 0.0
        total_rating = sum(review.rating() for review in self._reviews)
        return total_rating / len(self._reviews)

    def customers(self):
        return list({review.customer() for review in self._reviews})


class Review:
    _all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review._all_reviews.append(self)

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls._all_reviews

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant


customer1 = Customer("John", "Doe")
customer2 = Customer("Alice", "Smith")

restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

customer1.add_review(restaurant1, 5)
customer1.add_review(restaurant2, 4)
customer2.add_review(restaurant1, 3)
customer2.add_review(restaurant2, 5)

print("Average rating for Restaurant A:", restaurant1.average_star_rating())
print("Average rating for Restaurant B:", restaurant2.average_star_rating())

print("Customer 1 full name:", customer1.full_name())
print("Customer 2 full name:", customer2.full_name())

print("All customers:")
for customer in Customer.all():
    print(customer.full_name())

print("Customers who reviewed Restaurant A:")
for customer in restaurant1.customers():
    print(customer.full_name())

print("Customers with given name 'John':")
for customer in Customer.find_all_by_given_name("John"):
    print(customer.full_name())
