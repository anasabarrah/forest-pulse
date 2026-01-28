---
marp: true
theme: gaia
class: lead
backgroundColor: #0d1117
color: #e6edf3
style: |
  section {
    font-family: 'Arial', sans-serif;
  }
  h1 {
    color: #3fb950; /* Vert Néon */
    font-size: 80px;
  }
  h2 {
    color: #ffffff;
  }
  strong {
    color: #3fb950;
  }
  img {
    background-color: transparent;
  }
---

# FOREST PULSE
## Détection Hybride & Précoce

### 🛰️ Satellite + 📡 IoT

*Team Info & Elec - ActInSpace 2026*

---

# LE PROBLÈME
## L'Angle Mort Temporel

* **Sentinel-2** passe tous les **5 jours**.
* Un feu détruit **1 hectare** en **15 minutes**.

> **Problème :** L'information est précise, mais elle arrive trop tard.

---

# LA SOLUTION
## Architecture "Eye & Ear"

1.  👂 **L'OREILLE (Sol) :**
    * Capteurs IoT autonomes (LoRaWAN).
    * Détectent T° et Fumée en temps réel.

2.  👁️ **L'OEIL (Espace) :**
    * Alerte déclenche l'analyse Satellite ciblée.
    * Confirmation visuelle et cartographie.

---

# LA TECHNIQUE
## Algorithme de Fusion

**1. Physique :** Analyse de la signature spectrale (Chute Infrarouge).
**2. Mathématiques :** Indice NDVI & Dérivée Temporelle.

$$\Delta = NDVI_{t} - NDVI_{t-1}$$

**3. Système :** Edge Computing sur micro-contrôleur.

---

# PREUVE DE CONCEPT (POC)

*(Ici, insère ta capture d'écran Python avec les 3 images)*

* **Gauche :** Archive (Forêt saine)
* **Centre :** Alerte T0 (Début incendie)
* **Droite :** **Détection Algo (Zone Rouge)**

---

# LE MODÈLE ÉCO
## Une équation simple

$$\text{Coût Solution} \ll \text{Coût Incendie}$$

* **Hardware :** 50€ / Unité (Low cost)
* **Service :** Abonnement SaaS pour les Mairies/SDIS.
* **Rentabilité :** Immédiate dès le 1er feu évité.

---

# PRÊTS À DÉPLOYER

## L'Équipe
* **[Ton Prénom]** : Computer Science & Algo (Ex-MP)
* **[Prénom Pote]** : Electronics & IoT (Ex-MP)

### 🚀 Merci. Questions ?