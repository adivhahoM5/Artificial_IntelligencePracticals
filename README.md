# CMPG 313 – Artificial Intelligence Practicals
### North-West University | Module: CMPG 313

---

> **Note:** These are university practical assignments submitted as part of the CMPG 313 Artificial Intelligence module. They are not production projects — they are learning exercises meant to demonstrate understanding of core AI concepts.

---

## 📁 Project Structure

```
CMPG313-Practicals/
│
├── Practical_2/
│   └── practical2.py
│
├── Practical_3/
│   └── practical3.py
│
├── Practical_4/
│   └── healthbot.py
│
└── README.md
```

---

## Practical 2 – KMeans Clustering (2 Classes)

**Topic:** Unsupervised Machine Learning – KMeans Clustering

**Description:**
This practical introduces KMeans clustering using a synthetically generated two-class dataset. Two clusters of data points are generated around defined centers with added Gaussian noise to simulate real-world variation. The KMeans algorithm is then applied to group the data and the results are evaluated by comparing the predicted cluster labels to the true class labels.

**What it covers:**
- Generating synthetic datasets using NumPy
- Visualising data with Matplotlib scatter plots
- Applying KMeans clustering using Scikit-learn
- Aligning predicted cluster labels with true labels
- Calculating clustering accuracy

**Key Parameters:**
| Parameter | Value |
|---|---|
| Class 1 observations (N1) | 180 |
| Class 2 observations (N2) | 220 |
| Distance between centers (d) | 2.4 |
| Sigma 1 | 0.7 |
| Sigma 2 | 0.9 |
| Number of clusters | 2 |

**Expected Output:**
- Scatter plot of the generated dataset coloured by true class
- Clustering accuracy printed to the console

---

## Practical 3 – KMeans Clustering (3 Classes, Fitness Tracker Data)

**Topic:** Unsupervised Machine Learning – KMeans Clustering with Real-World Context

**Description:**
This practical extends the concepts from Practical 2 to a three-class clustering problem using a simulated fitness tracker dataset. Data points represent individuals characterised by their average steps per day and hours slept per night. The three clusters represent different activity levels: Active, Moderately Active, and Least Active. Random class sizes are used to simulate variability in real datasets.

**What it covers:**
- Generating multi-class synthetic datasets with random class sizes
- Simulating a real-world scenario (fitness tracking)
- Applying KMeans clustering to 3 clusters
- Labelling and interpreting clusters with meaningful names
- Computing and displaying per-cluster statistics (average steps and sleep)

**Key Parameters:**
| Parameter | Value |
|---|---|
| Class sizes (N1, N2, N3) | Random multiples of 100 (1–10) |
| Center 1 (Active) | 10 000 steps, 8.0 hrs sleep |
| Center 2 (Moderately Active) | 6 500 steps, 6.75 hrs sleep |
| Center 3 (Least Active) | 3 500 steps, 5.75 hrs sleep |
| Number of clusters | 3 |

**Expected Output:**
- Scatter plot of the generated dataset coloured by true class
- Clustering accuracy printed to the console
- Per-cluster average steps and sleep hours
- Scatter plot of KMeans clustering results

---

## Practical 4 – FOL-Based Healthcare Chatbot

**Topic:** First-Order Logic (FOL) – Rule-Based Expert System

**Description:**
This practical demonstrates the application of First-Order Logic in building a simple rule-based diagnostic chatbot. The chatbot accepts symptoms from the user, applies FOL-style inference rules stored in a knowledge base, and returns a probable diagnosis along with general advice. Several enhancements were added beyond the base requirements to improve the chatbot's functionality.

**What it covers:**
- Translating FOL rules into Python dictionary structures
- Implementing a simple FOL inference engine using subset matching
- Building an interactive command-line chatbot
- Debugging and fixing intentional errors in provided skeleton code
- Enhancing a base system with additional features

**Diseases in the Knowledge Base:**
| Disease | Required Symptoms |
|---|---|
| Flu | fever, cough, sore throat |
| Common Cold | sneezing, runny nose, mild fever |
| Malaria | fever, chills, sweating, headache |
| COVID-19 | fever, cough, shortness of breath, loss of taste |
| Strep Throat | sore throat, swollen lymph nodes, fever |

**Enhanced Features Added:**
1. **Simulation Disclaimer** — displayed at the start of every session
2. **Symptom Severity Rating** — user rates symptoms as Mild, Moderate, or Severe
3. **Follow-up Clarifying Questions** — narrows diagnosis when multiple diseases match
4. **Urgency Classification** — labels each diagnosis as Home Care, See a Doctor, or Emergency
5. **Unknown Symptom Detection** — warns user when an entered symptom is not recognised

**Expected Output:**
- Disclaimer banner
- Symptom input prompt
- Severity selection
- Diagnosis with urgency label and advice

---

## Technologies Used

| Practical | Technologies |
|---|---|
| Practical 2 | Python, NumPy, Matplotlib, Scikit-learn |
| Practical 3 | Python, NumPy, Matplotlib, Scikit-learn |
| Practical 4 | Python (standard library only) |

---

## How to Run

### Requirements
- Python 3.x
- For Practicals 2 & 3: `numpy`, `matplotlib`, `scikit-learn`

### Install dependencies (Practicals 2 & 3)
```bash
pip install numpy matplotlib scikit-learn
```

### Run each practical
```bash
# Practical 2
python Practical_2/practical2.py

# Practical 3
python Practical_3/practical3.py

# Practical 4
python Practical_4/healthbot.py
```

> Practicals 2 and 3 were originally developed in Google Colab and can also be run there by uploading the `.py` files or copying the code into a new notebook.

---

## Disclaimer
All code in this repository was written as part of university practical assignments for CMPG 313 at North-West University. These projects are for educational purposes only and are not intended for production use.
