class Car:
    def show_model(self):
        if hasattr(self, 'model'):  # mestipon: Check if attribute exists
            print("Model:", self.model)
        else:
            print("Error: 'model' attribute is missing.")

c = Car()
c.show_model()
