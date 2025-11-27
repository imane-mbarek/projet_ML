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

def arbre_decision_tester(request):
    return render(request,"arbre_decision/arbre_decision_form_c.html")

def arbre_decision_prediction(request):
    # Tâche 1 : Recevoir le Colis
    if request.method == 'POST':

        # Tâche 2 : Déballer le colis (extraction des données du formulaire)
        exerany = int(request.POST.get('exerany'))
        hlthplan = int(request.POST.get('hlthplan'))
        smoke100 = int(request.POST.get('smoke100'))
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        age = int(request.POST.get('age'))
        gender = int(request.POST.get('gender'))

        # Tâche 3 : Réveiller l'expert (charger le modèle Decision Tree)
        model = load_models('dt_class.pkl')

        # Tâche 4 : Poser la question à l'expert
        prediction = model.predict([[exerany, hlthplan, smoke100, height, weight, age, gender]])
        predicted_class = int(prediction[0])

        # Tâche 5 : Traduire la réponse
        health_label = {0: 'fair', 1: 'good'}
        imag_url = {
            'fair': 'images/camion.jpg',
            'good': 'images/touristique.jpg'
        }

        pred_health_state = health_label[predicted_class]
        pred_img = imag_url[pred_health_state]

        # Tâche 6 : Préparer le Plateau-Repas (context)
        input_data = {
            'exerany': exerany,
            'hlthplan': hlthplan,
            'smoke100': smoke100,
            'height': height,
            'weight': weight,
            'age': age,
            'gender': gender,
        }

        context = {
            'predicted_state': pred_health_state,
            'initial_data': input_data
        }

        return render(request, 'arbre_decision/arbre_decision_result_c.html', context)

    # Si GET : afficher le formulaire
    return render(request, 'arbre_decision/arbre_decision_form_c.html')



# pour la carte SVM -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def svm_details(request):
    return render(request,"svm/svm_details.html")

def svm_atelier_C(request):
    return render(request,"svm/svm_atelier_C.html")

def svm_atelier_R(request):
    return render(request,"svm/svm_atelier_R.html")

def svm_tester(request):
    return render(request,"svm/svm_form_c.html")

def svm_prediction(request):
# Tâche 1 : Recevoir le Colis
    if request.method == 'POST':
        
        
        # Tâche 2 : Déballer le colis (extraction des données du formulaire du béton)
        # Les valeurs sont des nombres flottants normalisés pour le modèle SVR
        ciment = float(request.POST.get('ciment'))
        eau = float(request.POST.get('eau'))
        sable = float(request.POST.get('sable'))
        gravier = float(request.POST.get('gravier'))
        age = float(request.POST.get('age')) # L'âge est aussi normalisé ici
        
        # Note: Les anciens champs (exerany, hlthplan, etc.) ont été supprimés/remplacés.
        
        # Tâche 3 : Réveiller l'expert (charger le modèle SVR)
        # Assurez-vous que 'svr_reg.pkl' est le bon chemin/nom de votre modèle SVR entraîné
        model = load_models('svm_reg.pkl')
        
        # La prédiction est une valeur continue (Résistance du Béton)
        prediction = model.predict([[ciment, eau, sable, gravier, age]])
        predicted_resistance = prediction[0]
        
        # Tâche 5 : Traduire la réponse (Simplifiée pour la régression)
        # Nous n'avons pas de classes à traduire, seulement une valeur numérique.
        
        # Tâche 6 : Préparer le Plateau-Repas (context)
        input_data = {
            'Ciment (norm.)': ciment,
            'Eau (norm.)': eau,
            'Sable (norm.)': sable,
            'Gravier (norm.)': gravier,
            'Âge (norm.)': age,
        }

        context = {
            # C'est la variable utilisée dans le template de résultat
            'predicted_resistance': predicted_resistance, 
            'initial_data': input_data,
            # Optionnel : Ajoutez une URL d'image pour le template de résultat
            'img_illustration': 'images/camion.jpg' 
        }   

        return render(request, 'svm/svm_result_c.html', context)

    # Si GET : afficher le formulaire
    return render(request, 'svm/svm_form_c.html')




# pour la carte random forest -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def random_forest_details(request):
    return render(request,"random_forest/random_forest_details.html")

def random_forest_atelier_C(request):
    return render(request,"random_forest/random_forest_atelier_C.html")

def random_forest_tester(request):
    return render(request,"random_forest/random_forest_form_c.html")

def random_forest_prediction(request):
    # Tâche 1 : Recevoir le Colis
    if request.method == 'POST':

        # Tâche 2 : Déballer le colis (extraction des données du formulaire)
        exerany = int(request.POST.get('exerany'))
        hlthplan = int(request.POST.get('hlthplan'))
        smoke100 = int(request.POST.get('smoke100'))
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        age = int(request.POST.get('age'))
        gender = int(request.POST.get('gender'))

        # Tâche 3 : Réveiller l'expert (charger le modèle Decision Tree)
        model = load_models('rf_class.pkl')

        # Tâche 4 : Poser la question à l'expert
        prediction = model.predict([[exerany, hlthplan, smoke100, height, weight, age, gender]])
        predicted_class = int(prediction[0])

        # Tâche 5 : Traduire la réponse
        health_label = {0: 'fair', 1: 'good'}
        imag_url = {
            'fair': 'images/camion.jpg',
            'good': 'images/touristique.jpg'
        }

        pred_health_state = health_label[predicted_class]
        pred_img = imag_url[pred_health_state]

        # Tâche 6 : Préparer le Plateau-Repas (context)
        input_data = {
            'exerany': exerany,
            'hlthplan': hlthplan,
            'smoke100': smoke100,
            'height': height,
            'weight': weight,
            'age': age,
            'gender': gender,
        }

        context = {
            'predicted_state': pred_health_state,
            'initial_data': input_data
        }

        return render(request, 'random_forest/random_forest_result_c.html', context)

    # Si GET : afficher le formulaire
    return render(request, 'random_forest/random_forest_form_c.html')


# pour la carte XGBoot -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def xgboost_details(request):
    return render(request,"xgboost/xgboost_details.html")

def xgboost_atelier_C(request):
    return render(request,"xgboost/xgboost_atelier_C.html")
