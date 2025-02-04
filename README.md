# Maths Project

## Description
This is a Django application designed for performing various mathematical operations. It provides an API for classifying numbers and other mathematical functionalities.

## Installation

1. Clone the repository:
   ```bash
   git clone <"https://github.com/cleoivvy/maths.git">
   cd <"C:\Users\clara\Documents\hng\backend\week2\maths">
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   SECRET_KEY=<django-insecure-s#tit&%e5m+=uy4p7wez(o8wt3@k90q%@xw1j$9+(=r$b)h&1>
   ALLOWED_HOSTS=maths-p2ah.onrender.com,localhost,127.0.0.1
   DATABASE_URL=<postgresql://maths_db_s1wk_user:OKsUPdYmx3ECqPj0UZBBpPshQrmKGDbl@dpg-cugu8o3tq21c73f4798g-a.oregon-postgres.render.com/maths_db_s1wk>
   ```

## Usage

To run the application, use the following command:
```bash
python manage.py runserver
```

You can access the API at `http://localhost:8000/`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
