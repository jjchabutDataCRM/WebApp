import streamlit as st
from vega_datasets import data
import matplotlib.pyplot as plt
import requests

CLIENT_ID = st.secrets["FT_CLIENT_ID"]
CLIENT_SECRET = st.secrets["FT_CLIENT_SECRET"]

class TokenManager:
    """Gère l'authentification et le renouvellement automatique du token"""
    
    def __init__(self):
        self.token = None
        self.expires_at = None
    
    def get_token(self) -> str:
        """Obtient un token valide (regénère si expiré)"""
        if self.token is None or datetime.now() >= self.expires_at:
            print("🔄 Génération d'un nouveau token...")
            
            url = "https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=%2Fpartenaire"
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = {
                "grant_type": "client_credentials",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "scope": "api_offresdemploiv2 o2dsoffre"
            }
            
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            
            self.token = response.json()["access_token"]
            self.expires_at = datetime.now() + timedelta(minutes=20)
            print("✓ Token généré")
        
        return self.token


source = data.cars()

if st.button("Call API"):
    st.text(CLIENT_ID)
    st.balloons()

if st.button("Dataset VEGA"):
    
	st.header("Visualization")

	st.subheader("Matplotlib")

	plt.figure(figsize=(12,8))
	plt.scatter(source['Horsepower'], source['Miles_per_Gallon'])
	st.pyplot(plt)
