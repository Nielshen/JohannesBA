import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import spearmanr
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


# Daten einlesen
df = pd.read_csv('johannes.csv', skiprows=[1])

print("Verfügbare Spalten:")
print(df.columns.tolist())

# Attention Check prüfen (AT01_01 sollte 4 sein)
df_clean = df[df['AT01_01'] == 4].copy()
print(f"\nUrsprüngliche Anzahl Zeilen: {len(df)}")
print(f"Zeilen nach Attention Check: {len(df_clean)}")

# Variablen definieren
variables = {
    # Digital Fluency (DF)
    'Digital_Fluency': ['DF01_01', 'DF01_02', 'DF01_03', 'DF02_01', 'DF02_02', 'DF02_03'],
    
    # Individual Creativity (IC)
    'Individual_Creativity': ['IC01_01', 'IC01_02', 'IC01_03', 'IC01_04', 'IC01_05', 
                            'IC01_06', 'IC01_07', 'IC02_08', 'IC02_09', 'IC02_10', 
                            'IC02_11', 'IC02_12', 'IC02_13'],
    
    # Job Complexity (JC)
    'Job_Complexity': ['JC01_01', 'JC01_02', 'JC01_03', 'JC01_04'],
    
    # Psychological Safety (PS)
    'Psychological_Safety': ['PS01_01', 'PS01_02', 'PS01_03', 'PS01_04', 'PS01_05'],
    
    # Supervisor Support (SS)
    'Supervisor_Support': ['SS01_01', 'SS01_02', 'SS01_03'],
    
    # Work Flexibility (WF)
    'Work_Flexibility': ['WF01_01', 'WF01_02', 'WF01_03', 'WF01_04', 'WF01_05', 'WF01_06'],
    
    # Work Method Autonomy (WM)
    'Work_Method_Autonomy': ['WM01_01', 'WM01_02', 'WM01_03']
}

# Mittelwerte für jede Variablengruppe berechnen
for var_group, columns in variables.items():
    df_clean[var_group] = df_clean[columns].mean(axis=1)


# Liste der aggregierten Variablen für die Analyse
variables_list = ['Digital_Fluency', 'Individual_Creativity', 
                 'Job_Complexity', 'Psychological_Safety', 'Supervisor_Support',
                 'Work_Flexibility', 'Work_Method_Autonomy']

# Dataframe für Analyse erstellen - hier war der Fehler
df_analysis = df_clean[variables_list]  # Wähle nur die berechneten Mittelwert-Spalten aus

df_analysis['Alter'] = df_clean['PF02_01']
df_analysis['Geschlecht'] = df_clean['PF01']

# Deskriptive Statistik für alle einzelnen Variablen
all_variables = []
for var_group, columns in variables.items():
    all_variables.extend(columns)

# Berechne Mittelwert und Standardabweichung für jede einzelne Frage
desc_stats = pd.DataFrame({
    'Mittelwert': df_clean[all_variables].mean(),
    'Std.-Abweichung': df_clean[all_variables].std()
})

print("\nDeskriptive Statistiken pro Frage:")
print(desc_stats.round(2))

print("\nDemografische Daten:")
print(f"Gender Verteilung (PF01):")
gender_counts = df_clean['PF01'].value_counts()
gender_percent = df_clean['PF01'].value_counts(normalize=True) * 100
for gender, count in gender_counts.items():
    print(f"Kategorie {gender}: {count} Teilnehmer ({gender_percent[gender]:.1f}%)")

print(f"\nAlter (PF02_01):")
print(f"Durchschnitt: {df_clean['PF02_01'].mean():.1f}")
print(f"Standardabweichung: {df_clean['PF02_01'].std():.1f}")
print(f"Minimum: {df_clean['PF02_01'].min()}")
print(f"Maximum: {df_clean['PF02_01'].max()}")

# Gruppenmittelwerte mit Standardabweichung
print("\nGruppenmittelwerte und Standardabweichungen:")
group_stats = {}
for var_group, columns in variables.items():
    # Berechne erst den Mittelwert pro Person für jede Gruppe
    group_means = df_clean[columns].mean(axis=1)
    group_stats[var_group] = {
        'Mittelwert': group_means.mean(),
        'Std.-Abweichung': group_means.std()
    }

stats_df = pd.DataFrame(group_stats).T
print(stats_df.round(2))

def calculate_pvalues(df):
    """
    Berechnet p-Werte für Korrelationen zwischen allen Spalten im DataFrame
    """
    df = df.dropna()
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    
    for r in df.columns:
        for c in df.columns:
            pvalues[r][c] = stats.pearsonr(df[r], df[c])[1]
            
    return pvalues.round(3)

# Korrelationsmatrix und p-Werte berechnen
corr_matrix = df_analysis.corr().round(2)
p_values = calculate_pvalues(df_analysis)

# Formatierte Ausgabe mit Signifikanzniveaus
def format_with_stars(corr, p):
    if p < 0.01:
        return f"{corr}**"
    elif p < 0.05:
        return f"{corr}*"
    return f"{corr}"

def cronbach_alpha(df, items):
    """
    Berechnet Cronbachs Alpha für eine Gruppe von Items
    """
    # Anzahl der Items
    k = len(items)
    
    # Wenn nur ein Item vorhanden ist, kann kein Alpha berechnet werden
    if k < 2:
        return None
    
    # Varianz der Summenscores
    total_var = df[items].sum(axis=1).var()
    
    # Summe der Varianzen der einzelnen Items
    item_vars = df[items].var().sum()
    
    # Cronbachs Alpha Formel
    alpha = (k / (k-1)) * (1 - item_vars / total_var)
    
    return alpha

# Cronbachs Alpha für jede Variablengruppe berechnen
print("\nCronbachs Alpha für alle Skalen:")
for var_group, columns in variables.items():
    alpha = cronbach_alpha(df_clean, columns)
    print(f"{var_group}: {alpha:.3f}")


# Erstelle formatierte Korrelationsmatrix mit Sternchen
formatted_corr = pd.DataFrame(index=corr_matrix.index, columns=corr_matrix.columns)
for i in corr_matrix.index:
    for j in corr_matrix.columns:
        formatted_corr.loc[i,j] = format_with_stars(corr_matrix.loc[i,j], p_values.loc[i,j])

# Vollständige Matrix ausgeben
pd.set_option('display.max_columns', None)  # Zeige alle Spalten
pd.set_option('display.width', None)        # Keine Zeilenumbrüche
print("\nKorrelationsmatrix mit Signifikanzniveaus:")
print("Anmerkung: *p < 0.05; **p < 0.01")
print(formatted_corr)

# Deskriptive Statistik
desc_stats_corr = pd.DataFrame({
    'Mittelwert': df_analysis[variables_list].mean(),
    'Std.-Abweichung': df_analysis[variables_list].std()
})

print("\nDeskriptive Statistiken:")
print(desc_stats_corr.round(2))
# Heatmap der Korrelationen mit seaborn erstellen

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, 
            annot=True, 
            cmap='RdBu_r',
            vmin=-1, 
            vmax=1,
            center=0,
            square=True)
plt.title('Korrelationsmatrix (Heatmap)')
plt.tight_layout()
plt.savefig('korrelationsmatrix.png', dpi=300, bbox_inches='tight')
plt.close()

# Standardisierung der kontinuierlichen Variablen (Z-Standardisierung)
def standardize(x):
    return (x - x.mean()) / x.std()

# Variablen standardisieren
df_analysis['Work_Flexibility_z'] = standardize(df_analysis['Work_Flexibility'])
df_analysis['Digital_Fluency_z'] = standardize(df_analysis['Digital_Fluency'])
df_analysis['Supervisor_Support_z'] = standardize(df_analysis['Supervisor_Support'])
df_analysis['Psychological_Safety_z'] = standardize(df_analysis['Psychological_Safety'])
df_analysis['Job_Complexity_z'] = standardize(df_analysis['Job_Complexity'])
df_analysis['Work_Method_Autonomy_z'] = standardize(df_analysis['Work_Method_Autonomy'])
df_analysis['Alter_z'] = standardize(df_analysis['Alter'])

# Interaktionsterme erstellen
df_analysis['WF_x_DF'] = df_analysis['Work_Flexibility_z'] * df_analysis['Digital_Fluency_z']
df_analysis['WF_x_SS'] = df_analysis['Work_Flexibility_z'] * df_analysis['Supervisor_Support_z']

# Hierarchische Regression
# Modell 1: Kontrollvariablen
X1 = sm.add_constant(df_analysis[['Alter_z', 'Geschlecht', 'Psychological_Safety_z', 
                                 'Job_Complexity_z', 'Work_Method_Autonomy_z']])
y = df_analysis['Individual_Creativity']
model1 = sm.OLS(y, X1).fit()

# Modell 2: Haupteffekte
X2 = sm.add_constant(df_analysis[['Alter_z', 'Geschlecht', 'Psychological_Safety_z', 
                                 'Job_Complexity_z', 'Work_Method_Autonomy_z',
                                 'Work_Flexibility_z', 'Digital_Fluency_z', 'Supervisor_Support_z']])
model2 = sm.OLS(y, X2).fit()

# Modell 3: Interaktionseffekte
X3 = sm.add_constant(df_analysis[['Alter_z', 'Geschlecht', 'Psychological_Safety_z', 
                                 'Job_Complexity_z', 'Work_Method_Autonomy_z',
                                 'Work_Flexibility_z', 'Digital_Fluency_z', 'Supervisor_Support_z',
                                 'WF_x_DF', 'WF_x_SS']])
model3 = sm.OLS(y, X3).fit()

# Ergebnisse ausgeben
print("\nModell 1 - Kontrollvariablen:")
print(model1.summary().tables[1])

print("\nModell 2 - Haupteffekte:")
print(model2.summary().tables[1])

print("\nModell 3 - Interaktionseffekte:")
print(model3.summary().tables[1])

# R-Quadrat Veränderungen
print("\nR-Quadrat Werte:")
print(f"Modell 1 R²: {model1.rsquared:.3f}")
print(f"Modell 2 R²: {model2.rsquared:.3f}")
print(f"Modell 3 R²: {model3.rsquared:.3f}")

# Funktion für Simple Slopes Plot
# Funktion für Simple Slopes Plot
def plot_interaction(moderator_name, predictor_name, outcome_name):
    plt.figure(figsize=(10, 6))
    
    # Erstelle High/Low Werte für Moderator und Predictor
    moderator_high = df_analysis[f'{moderator_name}_z'].mean() + df_analysis[f'{moderator_name}_z'].std()
    moderator_low = df_analysis[f'{moderator_name}_z'].mean() - df_analysis[f'{moderator_name}_z'].std()
    pred_range = np.linspace(df_analysis[f'{predictor_name}_z'].min(), 
                           df_analysis[f'{predictor_name}_z'].max(), 100)
    
    # Berechne vorhergesagte Werte
    y_high = model3.params['const'] + \
             model3.params[f'{predictor_name}_z'] * pred_range + \
             model3.params[f'{moderator_name}_z'] * moderator_high + \
             model3.params[f'WF_x_DF' if moderator_name == 'Digital_Fluency' else 'WF_x_SS'] * pred_range * moderator_high
    
    y_low = model3.params['const'] + \
            model3.params[f'{predictor_name}_z'] * pred_range + \
            model3.params[f'{moderator_name}_z'] * moderator_low + \
            model3.params[f'WF_x_DF' if moderator_name == 'Digital_Fluency' else 'WF_x_SS'] * pred_range * moderator_low
    
    # Plotten
    plt.plot(pred_range, y_high, 'b-', label=f'High {moderator_name} (+1 SD)')
    plt.plot(pred_range, y_low, 'r--', label=f'Low {moderator_name} (-1 SD)')
    
    plt.xlabel(predictor_name.replace('_', ' '))
    plt.ylabel(outcome_name.replace('_', ' '))
    plt.title(f'Interaction Effect of {predictor_name} and {moderator_name}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f'interaction_{moderator_name}.png', dpi=300, bbox_inches='tight')
    plt.close()

# Plots erstellen
plot_interaction('Digital_Fluency', 'Work_Flexibility', 'Individual_Creativity')
plot_interaction('Supervisor_Support', 'Work_Flexibility', 'Individual_Creativity')

# Haupteffekt visualisieren
plt.figure(figsize=(10, 6))
sns.regplot(x='Work_Flexibility', y='Individual_Creativity', data=df_analysis)
plt.title('Haupteffekt: Work Flexibility auf Individual Creativity')
plt.savefig('main_effect.png', dpi=300, bbox_inches='tight')
plt.close()