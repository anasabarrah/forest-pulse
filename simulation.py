import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# --- 1. CONFIGURATION ---
N = 200  # Taille de la zone (200x200 pixels)
np.random.seed(42) # Pour que le résultat soit toujours le même (effet démo)

# Création d'une colormap personnalisée (Rouge = Danger, Vert = Forêt)
colors = [(0.8, 0, 0), (1, 1, 0), (0, 0.5, 0)] # Rouge -> Jaune -> Vert
cm = LinearSegmentedColormap.from_list("NDVI_Map", colors, N=100)

# --- 2. SIMULATION DES DONNÉES ---

# ÉTAT 1 : SEMAINE DERNIÈRE (Tout va bien)
# Génère une forêt dense (valeurs proches de 0.8) avec un peu de bruit naturel
forest_base = np.random.normal(0.75, 0.1, (N, N))
forest_base = np.clip(forest_base, 0, 1) # On garde entre 0 et 1

# ÉTAT 2 : AUJOURD'HUI (Incident)
current_state = forest_base.copy()
# Simulation d'un feu : on écrase une zone avec des valeurs très basses (0.1)
# On fait une forme un peu organique (pas juste un carré)
Y, X = np.ogrid[:N, :N]
dist_from_center = np.sqrt((X - 100)**2 + (Y - 100)**2)
mask_fire = dist_from_center < 40 # Cercle de feu rayon 40
# On ajoute du bruit au feu
fire_damage = np.random.normal(0.15, 0.05, (N, N))
current_state[mask_fire] = fire_damage[mask_fire]

# --- 3. ALGORITHME DE DÉTECTION (Ton code Ingénieur) ---

# Calcul du delta (Changement)
delta = current_state - forest_base

# Seuil d'alerte : Si chute de plus de 0.4 points de NDVI
ALERTE_SEUIL = -0.4
detection_mask = delta < ALERTE_SEUIL

# --- 4. VISUALISATION DASHBOARD ---
fig, ax = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle(f"SYSTÈME DE DÉTECTION HYBRIDE - FOREST PULSE", fontsize=16, fontweight='bold')

# Plot 1 : Situation J-5
ax[0].imshow(forest_base, cmap=cm, vmin=0, vmax=1)
ax[0].set_title("Archive Satellite (J-5)\nÉtat Normal")
ax[0].axis('off')

# Plot 2 : Situation J (Temps Réel)
ax[1].imshow(current_state, cmap=cm, vmin=0, vmax=1)
ax[1].set_title("Acquisition Satellite (T0 + 15min)\nAprès Alerte Capteur IoT")
ax[1].axis('off')

# Plot 3 : Analyse Algorithmique
# On affiche en noir et blanc, et le feu en rouge vif
result_map = np.zeros((N, N, 3)) # Image RGB noire
result_map[detection_mask] = [1, 0, 0] # Zone détectée en ROUGE

ax[2].imshow(result_map)
ax[2].set_title("ANALYSE AUTOMATIQUE\nZone d'intervention prioritaire")
ax[2].axis('off')

plt.tight_layout()
plt.show()