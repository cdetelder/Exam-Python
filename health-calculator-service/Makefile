IMAGE_NAME=health-calculator-service
PORT=5000

.PHONY: init run test build clean

init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

build:
	@echo "Building the Docker image..."
	docker build -t $(IMAGE_NAME) .

run:
	@echo "Running the Flask app..."
	docker run -p $(PORT):5000 $(IMAGE_NAME)

test:
	@echo "Running tests inside Docker..."
	docker run --rm $(IMAGE_NAME) python -m unittest discover

clean:
	@echo "Cleaning up..."
	docker system prune -f
