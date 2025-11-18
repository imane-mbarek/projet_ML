from django.shortcuts import render
import os
import joblib # type: ignore

# Create your views here.
# pour la carte régression logistique --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def index(request):
    return render(request,"index.html") 

def regLog_details(request):
    return render(request,"regLog/regLog_details.html")

def regLog_atelier_C(request):
    return render(request,"regLog/regLog_atelier_C.html")

def regLog_tester(request):
    return render(request,"regLog/vehicles_form.html")

def load_models(name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, 'models_ai')
    model_path = os.path.join(models_dir, name)

    ml_model = joblib.load(model_path)
    return ml_model


def regLog_prediction(request):
    # Tâche 1 : Recevoir le Colis
    if request.method == 'POST':
        # Tâche 2 : Déballer le Colis
        hauteur = float(request.POST.get('hauteur'))
        nbr_roues = float(request.POST.get('Nombre_de_roues'))

        # Tâche 3 : Réveiller l’Expert
        # (cette fonction load_models() est définie avant)
        model = load_models('logreg_model.pkl')

        # Tâche 4 : Poser la Question à l’Expert
        prediction = model.predict([[hauteur, nbr_roues]])
        predicted_class = prediction[0]

        # Tâche 5 : Traduire la Réponse
        type_vehicules = {0: 'Camion', 1: 'Touristique'}
        img_url = {
            'Camion': 'images/camion.jpg',
            'Touristique': 'images/touristique.jpg'
        }

        pred_vehicle = type_vehicules[predicted_class]
        pred_img = img_url[pred_vehicle]

        # Tâche 6 : Préparer le Plateau-Repas (context)
        input_data = {
            'hauteur': hauteur,
            'nbr_roues': nbr_roues
        }

        context = {
            'type_vehicule': pred_vehicle,
            'img_vehicule': pred_img,
            'initial_data': input_data
        }

        return render(request, 'regLog/reglog_results.html', context)

    return render(request, 'regLog/vehicles_form.html')




# pour la carte arbre décision --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def arbre_decision_details(request):
    return render(request,"arbre_decision/arbre_decision_details.html")

def arbre_atelier_C(request):
    return render(request,"arbre_decision/arbre_atelier_C.html")



# pour la carte SVM -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def svm_details(request):
    return render(request,"svm/svm_details.html")

def svm_atelier_C(request):
    return render(request,"svm/svm_atelier_C.html")

def svm_atelier_R(request):
    return render(request,"svm/svm_atelier_R.html")


# pour la carte random forest -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def random_forest_details(request):
    return render(request,"random_forest/random_forest_details.html")

def random_forest_atelier_C(request):
    return render(request,"random_forest/random_forest_atelier_C.html")

# pour la carte XGBoot -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def xgboost_details(request):
    return render(request,"xgboost/xgboost_details.html")

def xgboost_atelier_C(request):
    return render(request,"xgboost/xgboost_atelier_C.html")
