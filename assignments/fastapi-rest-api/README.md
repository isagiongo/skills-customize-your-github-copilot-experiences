# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework, including request handling, response models, validation, and CRUD operations.

## 📝 Tasks

### 🛠️ Define the API models

#### Description
Create Pydantic models for your API resources and use them to validate incoming request data.

#### Requirements
Completed program should:

- Define a `Pydantic` model for the resource data
- Use the model for request validation and response serialization
- Include at least one required field and one optional field

### 🛠️ Implement CRUD endpoints

#### Description
Build REST endpoints that allow clients to create, read, update, and delete resource items.

#### Requirements
Completed program should:

- Include endpoints for `GET`, `POST`, `PUT`, and `DELETE`
- Return appropriate HTTP status codes for each operation
- Allow creating new items and storing them in memory
- Allow updating existing items by ID
- Allow deleting items by ID

### 🛠️ Add request validation and feedback

#### Description
Provide clear validation errors and success messages when the API receives invalid or successful requests.

#### Requirements
Completed program should:

- Validate incoming JSON data using FastAPI and Pydantic
- Return error responses for invalid input
- Return success responses that include created or updated resource details
- Handle missing item IDs with a 404 response
