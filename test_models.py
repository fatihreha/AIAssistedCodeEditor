# test_models.py
import ai_service

if __name__ == "__main__":
    models = ai_service.list_available_models()
    print("Kullanılabilir Modeller:")
    print(models)