# FastAPI Dataset Processing API

A FastAPI-based REST API for loading, viewing, and preprocessing text datasets. This API provides endpoints for dataset loading, normalization, and line-by-line access to the data.

## Features

- Load text datasets from file
- View dataset status and contents
- Text normalization preprocessing:
  - Lowercase conversion
  - Punctuation removal
  - Whitespace standardization
  - Format standardization
- Line-by-line data access
- Error handling for missing files and invalid requests
- Text augmentation to introduce spelling errors

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd fastapi-app
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

## API Endpoints

### Root Endpoint
- `GET /`: Welcome message and available endpoints

### Dataset Operations
- `POST /load`: Load the dataset from file sample.txt
- `GET /view`: View the dataset
- `GET /normalize`: View normalized version of the dataset
- `GET /augment`: Augmented dataset

## Example Requests

### Load Dataset

```bash
curl -X POST http://localhost:8000/load
```

Response:

```json
{
    "message": "Dataset loaded successfully",
    "total_lines": 5
}
```

### Get Normalized Dataset

```bash
curl http://localhost:8000/dataset/normalize
```


## Project Structure

```
fastapi-app/
├── main.py           # Main FastAPI application
├── requirements.txt  # Project dependencies
├── sample.txt       # Sample dataset file
└── README.md        # Project documentation
```

## Dependencies

- FastAPI
- Uvicorn
- Python 3.7+

## Error Handling

The API includes proper error handling for common scenarios:

- 404: Dataset file not found
- 400: Dataset not loaded
- Line number out of range errors

## Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Run

- uvicorn main:app --reload
- curl -X POST http://localhost:8000/load from the folder containing sample.txt to load the data
- other endpoints: view
- http://localhost:8000/
