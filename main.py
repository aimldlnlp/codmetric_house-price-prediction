from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import train_model
from src.evaluate import evaluate_model

def main():
    data_path = "data/housing.csv"
    df = load_data(data_path)
    X_train, X_test, y_train, y_test = preprocess_data(df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
