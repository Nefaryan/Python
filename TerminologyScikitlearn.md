# Terminologia Scikit-learn: Guida Completa

## Concetti Fondamentali

### Machine Learning

**Apprendimento automatico (Machine Learning)**: Disciplina dell'intelligenza artificiale che si concentra sullo sviluppo di algoritmi e modelli che permettono ai computer di "imparare" dai dati. Invece di seguire istruzioni esplicite, un modello di machine learning identifica pattern, relazioni e insight direttamente dai dati per fare previsioni o prendere decisioni. L'obiettivo finale è la **generalizzazione**, ovvero la capacità del modello di performare accuratamente su dati nuovi e mai visti prima. Si suddivide principalmente in apprendimento supervisionato, non supervisionato e per rinforzo.

### Classificazione

**Classificazione (Classification)**: Compito di apprendimento supervisionato in cui l'obiettivo è predire un'etichetta di classe discreta (una categoria) per un dato input. Il modello impara da un dataset in cui ogni esempio è già etichettato. Esempi includono il riconoscimento di spam (spam/non-spam), la diagnosi medica (malato/sano) o il riconoscimento di immagini (gatto/cane). Algoritmi comuni includono la Regressione Logistica, le Support Vector Machines (SVM) e gli Alberi Decisionali.

### Regressione

**Regressione (Regression)**: Compito di apprendimento supervisionato in cui l'obiettivo è predire un valore numerico continuo. A differenza della classificazione, l'output non è una categoria, ma una quantità. Esempi includono la previsione del prezzo di un immobile, la stima della temperatura di domani o la previsione delle vendite future. Algoritmi comuni sono la Regressione Lineare, la Support Vector Regression (SVR) e i modelli basati su alberi come Random Forest.

### Raggruppamento

**Raggruppamento (Clustering)**: Compito di apprendimento non supervisionato in cui l'obiettivo è raggruppare un insieme di oggetti in modo tale che gli oggetti nello stesso gruppo (chiamato cluster) siano più simili tra loro rispetto a quelli in altri gruppi. A differenza della classificazione, non si dispone di etichette predefinite; l'algoritmo scopre autonomamente la struttura e le categorie nascoste nei dati. Esempi includono la segmentazione dei clienti in base al comportamento d'acquisto o il raggruppamento di documenti per argomento. Algoritmi comuni includono K-Means, DBSCAN e il clustering gerarchico.

### Feature

**Caratteristiche (Features)**: Le variabili indipendenti o attributi misurabili che descrivono ogni singolo campione (o riga) nel dataset. Sono l'input che il modello utilizza per fare una previsione. Ad esempio, in un dataset per la previsione del prezzo di una casa, le feature potrebbero essere la superficie in metri quadri, il numero di stanze e l'età dell'edificio. La qualità e la rilevanza delle feature sono cruciali per le prestazioni del modello.

### Target/Label

**Variabile dipendente (Target/Label)**: La variabile che il modello cerca di predire. È l'output desiderato. Nei problemi di classificazione, viene spesso chiamata **label** (etichetta) ed è di natura categorica (es. "spam"). Nei problemi di regressione, è chiamata **target** (obiettivo) ed è di natura numerica continua (es. 150.000€). È la "risposta corretta" che il modello usa per apprendere durante la fase di addestramento supervisionato.

### Dataset

**Set di dati (Dataset)**: Una raccolta organizzata di dati, tipicamente strutturata in forma tabellare dove le righe rappresentano i campioni (o esempi) e le colonne rappresentano le feature e la variabile target. Un dataset è la risorsa fondamentale per qualsiasi progetto di machine learning, poiché viene utilizzato per addestrare, validare e testare i modelli. La sua qualità, dimensione e rappresentatività del problema reale influenzano direttamente il risultato finale.

---

## Pipeline di Machine Learning

### Pipeline

**Pipeline (Catena di montaggio)**: Un oggetto di scikit-learn che permette di concatenare in sequenza più passaggi di un flusso di lavoro di machine learning (es. pre-elaborazione e classificazione) in un unico stimatore. La Pipeline incapsula una serie di trasformatori (come `StandardScaler` o `PCA`) e un modello finale (come `SVC` o `LinearRegression`).

I suoi vantaggi principali sono:

- **Convenienza**: Semplifica il codice raggruppando tutti i passaggi in un unico oggetto. Chiamando `.fit()` sulla pipeline, si eseguono in sequenza il `fit_transform()` di ogni passaggio intermedio e il `.fit()` del modello finale.
- **Prevenzione del "Data Leakage"**: È il suo vantaggio più importante. Durante la validazione incrociata, la pipeline garantisce che i dati di validazione non vengano usati per "addestrare" i passaggi di pre-elaborazione (es. calcolare la media per lo `StandardScaler`), prevenendo una stima ottimistica delle prestazioni.
- **Ottimizzazione degli Iperparametri**: Può essere usata direttamente con `GridSearchCV` per ottimizzare simultaneamente gli iperparametri di tutti i componenti della catena, sia quelli di pre-elaborazione che quelli del modello finale.

### Training Set

**Set di addestramento (Training Set)**: La porzione più grande del dataset originale (tipicamente 70-80%) utilizzata per addestrare il modello. Durante questa fase, l'algoritmo analizza i dati di addestramento per identificare le relazioni sottostanti tra le feature di input e la variabile target. L'obiettivo è "insegnare" al modello a riconoscere i pattern che gli permetteranno di fare previsioni accurate. La qualità e la quantità dei dati di training sono fondamentali per le prestazioni finali del modello.

### Test Set

**Set di test (Test Set)**: Una porzione del dataset (tipicamente 20-30%) che viene tenuta completamente separata durante la fase di addestramento. Viene utilizzata solo alla fine del processo per valutare le prestazioni del modello addestrato. Poiché il modello non ha mai "visto" questi dati, il test set fornisce una stima imparziale della sua capacità di **generalizzazione** su dati nuovi e sconosciuti, simulando l'applicazione nel mondo reale.

### Preprocessing

**Pre-elaborazione (Preprocessing)**: Fase cruciale che consiste nel pulire, trasformare e preparare i dati grezzi prima di fornirli al modello. Questo processo include una serie di tecniche come la gestione dei valori mancanti (imputazione), la scalatura delle feature numeriche (es. `StandardScaler`), la codifica delle variabili categoriche (es. `OneHotEncoder`) e la creazione di nuove feature (feature engineering). Un buon preprocessing è essenziale perché la qualità dei dati influenza direttamente la capacità del modello di apprendere.

### Fit

**Addestramento (Fit)**: Il processo fondamentale in cui il modello "impara" dai dati. In scikit-learn, questo viene eseguito chiamando il metodo `.fit(X_train, y_train)` su un oggetto modello. Durante il `fit`, l'algoritmo regola i suoi parametri interni (es. i coefficienti in una regressione lineare) per minimizzare l'errore tra le sue previsioni e i valori reali presenti nel training set. È il cuore del processo di apprendimento automatico.

### Predict

**Predizione (Predict)**: Una volta che il modello è stato addestrato tramite il metodo `.fit()`, può essere utilizzato per fare previsioni su nuovi dati. Chiamando il metodo `.predict(X_test)`, si forniscono al modello nuovi campioni (senza le relative etichette) e lui restituisce le previsioni corrispondenti (classi o valori continui). Questo è il passo in cui il modello applica ciò che ha imparato per generare output utili.

---

## Preprocessing e Trasformazione Dati

### Scaling

**Scalatura (Scaling)**: Processo fondamentale di pre-elaborazione che consiste nel trasformare le feature numeriche per portarle su una scala di valori comune. Molti algoritmi di machine learning (come SVM, k-NN e modelli lineari con regolarizzazione) sono sensibili alla scala delle feature di input. Se una feature ha un range di valori molto più ampio di altre, può dominare il processo di apprendimento. La scalatura assicura che tutte le feature contribuiscano in modo equo al risultato, migliorando la convergenza e le prestazioni del modello.

### StandardScaler

**Standardizzazione (StandardScaler)**: Una delle tecniche di scalatura più comuni. Trasforma ogni feature sottraendo la sua media (μ) e dividendola per la sua deviazione standard (σ). La formula è: `z = (x - μ) / σ`. Il risultato è una distribuzione con media 0 e deviazione standard 1. Questa tecnica non vincola i valori a un range specifico ed è meno sensibile agli outlier rispetto alla normalizzazione Min-Max. È la scelta di default per molti algoritmi che assumono dati centrati attorno allo zero.

### MinMaxScaler

**Normalizzazione Min-Max (MinMaxScaler)**: Tecnica di scalatura che trasforma i dati in un intervallo predefinito, solitamente [0, 1]. La formula è: `x' = (x - min(x)) / (max(x) - min(x))`. Ogni valore viene riproporzionato in base al valore minimo e massimo della feature. È utile quando l'algoritmo richiede dati in un range specifico (es. reti neurali) o quando si vuole preservare la distribuzione originale dei dati. Tuttavia, è molto sensibile alla presenza di outlier, poiché `min` e `max` possono essere distorti da valori anomali.

### One-Hot Encoding

**Codifica One-Hot (One-Hot Encoding)**: Tecnica per convertire variabili categoriche nominali (senza un ordine intrinseco) in un formato numerico che i modelli di machine learning possono interpretare. Per ogni categoria unica presente nella feature originale, viene creata una nuova colonna binaria (dummy variable). Questa colonna avrà valore 1 se il campione appartiene a quella categoria, e 0 altrimenti. Questo evita che il modello interpreti erroneamente un ordine numerico tra le categorie (es. "rosso" < "verde" < "blu").

### Imputation

**Imputazione (Imputation)**: Processo di gestione dei valori mancanti (NaN) in un dataset. Poiché la maggior parte degli algoritmi di machine learning non può gestire dati mancanti, è necessario sostituirli con valori stimati. Le strategie più semplici includono la sostituzione con la media (per dati numerici), la mediana (più robusta agli outlier) o la moda (per dati categorici). Esistono anche tecniche più avanzate, come l'imputazione basata sui k-nearest neighbors (k-NN) o su modelli predittivi.

---

## Validazione e Selezione del Modello

### SVC (Support Vector Classifier)

**Classificatore a Vettori di Supporto (Support Vector Classifier)**: L'implementazione dell'algoritmo Support Vector Machine (SVM) per compiti di classificazione. L'obiettivo di SVC è trovare l'iperpiano ottimale che separa i punti dati di diverse classi massimizzando il margine tra di esse. Grazie al "trucco del kernel", può gestire efficacemente dati non linearmente separabili, mappandoli in uno spazio dimensionale superiore dove una separazione lineare diventa possibile. I suoi iperparametri chiave includono `C` (parametro di regolarizzazione, che bilancia tra un margine ampio e la corretta classificazione dei punti di training), `kernel` (es. 'linear', 'rbf', 'poly') e `gamma` (per i kernel non lineari).

### Parametro C (Regularization Parameter)

**Parametro di regolarizzazione (C)**: Iperparametro fondamentale negli algoritmi Support Vector Machine (SVM). Controlla il compromesso tra ottenere un margine di separazione più ampio e classificare correttamente il maggior numero possibile di punti di addestramento.

- Un **valore basso di `C`** aumenta la tolleranza per i punti classificati erroneamente, portando a un **margine più ampio** e a un modello più semplice (maggiore regolarizzazione). Questo può aiutare a prevenire l'overfitting.
- Un **valore alto di `C`** impone una penalità maggiore per ogni errore di classificazione, costringendo il modello a trovare un **margine più stretto** che cerchi di classificare correttamente tutti i punti. Questo può portare a un modello più complesso e al rischio di overfitting.
In sostanza, `C` è l'inverso della forza di regolarizzazione: `C` piccolo = regolarizzazione forte; `C` grande = regolarizzazione debole.

### Cross-Validation

**Validazione incrociata (Cross-Validation)**: Tecnica di valutazione robusta che fornisce una stima più affidabile delle prestazioni di un modello rispetto a una singola suddivisione train-test. Il metodo più comune è la **k-fold cross-validation**: il training set viene diviso in *k* sottoinsiemi (fold). Il modello viene addestrato e valutato *k* volte; a ogni iterazione, un fold diverso viene usato come set di validazione e i restanti *k-1* come training set. La metrica di performance finale è la media dei risultati ottenuti in ogni fold. Questo processo riduce la variabilità del risultato e fornisce una misura più accurata della capacità di generalizzazione del modello.

### Grid Search

**Ricerca a griglia (Grid Search)**: Metodo esaustivo per l'ottimizzazione degli iperparametri. Si definisce una "griglia" di valori possibili per ogni iperparametro che si desidera ottimizzare. L'algoritmo addestra e valuta un modello per ogni singola combinazione di iperparametri presente nella griglia. Al termine, restituisce la combinazione che ha prodotto le migliori prestazioni. Sebbene sia molto accurato, questo metodo può diventare computazionalmente molto costoso ("maledizione della dimensionalità") se il numero di iperparametri e dei loro possibili valori è elevato.

### Random Search

**Ricerca casuale (Random Search)**: Alternativa efficiente alla Grid Search per l'ottimizzazione degli iperparametri. Invece di testare tutte le combinazioni possibili, la ricerca casuale campiona un numero fisso di combinazioni da distribuzioni statistiche specificate per ogni iperparametro. Spesso, riesce a trovare combinazioni di iperparametri molto buone (o addirittura migliori) in una frazione del tempo richiesto dalla Grid Search, poiché non spreca iterazioni su iperparametri poco influenti e può esplorare un range di valori più ampio.

### Hyperparameters

**Iperparametri (Hyperparameters)**: Parametri di configurazione di un modello che non vengono appresi direttamente dai dati durante il processo di addestramento, ma devono essere impostati a priori. Controllano il comportamento dell'algoritmo di apprendimento stesso. Esempi includono il `learning_rate` nel Gradient Boosting, il parametro di regolarizzazione `alpha` nei modelli lineari, il numero di vicini `n_neighbors` in k-NN o il tipo di `kernel` in una SVM. La scelta ottimale degli iperparametri è cruciale per le prestazioni del modello e viene effettuata tramite tecniche come Grid Search o Random Search.

### Overfitting

**Sovradattamento (Overfitting)**: Fenomeno che si verifica quando un modello di machine learning è eccessivamente complesso e "impara a memoria" i dati di addestramento, inclusi il rumore e le fluttuazioni casuali. Un modello in overfitting mostra prestazioni eccellenti sul training set ma scarse su dati nuovi e mai visti (bassa capacità di generalizzazione). È il risultato di un modello con troppa capacità rispetto alla quantità di dati. Tecniche come la regolarizzazione, la cross-validation e l'aumento dei dati di training sono utilizzate per mitigarlo.

### Underfitting

**Sottoadattamento (Underfitting)**: Fenomeno opposto all'overfitting, che si verifica quando un modello è troppo semplice per catturare la struttura sottostante dei dati. Un modello in underfitting ha scarse prestazioni sia sul training set che sul test set, poiché non è in grado di apprendere le relazioni significative tra le feature e il target. Solitamente indica che il modello scelto non è sufficientemente complesso o che le feature utilizzate non sono abbastanza informative.

---

## Riduzione della Dimensionalità

### Dimensionality Reduction

**Riduzione della dimensionalità**: Processo di riduzione del numero di feature (variabili) in un dataset. L'obiettivo è semplificare il modello, ridurre i tempi di calcolo e mitigare la "maledizione della dimensionalità" (curse of dimensionality), preservando al contempo la maggior quantità possibile di informazione rilevante. Si divide principalmente in due approcci: selezione delle feature (feature selection) e estrazione delle feature (feature extraction).

### PCA (Principal Component Analysis)

**Analisi delle Componenti Principali**: Tecnica di estrazione di feature non supervisionata che trasforma i dati in un nuovo sistema di coordinate. Le nuove feature, chiamate componenti principali, sono combinazioni lineari delle feature originali, sono ortogonali tra loro e sono ordinate in base alla quantità di varianza dei dati che riescono a "spiegare". Le prime componenti catturano la massima varianza possibile, permettendo di scartare le successive con perdita minima di informazione.

### Explained Variance

**Varianza spiegata**: Metrica associata a ciascuna componente principale in PCA che indica la proporzione della varianza totale del dataset catturata da quella componente. Analizzando la varianza spiegata cumulativa, è possibile decidere quante componenti principali mantenere per raggiungere un compromesso desiderato tra riduzione della dimensionalità e conservazione dell'informazione.

### ICA (Independent Component Analysis)

**Analisi delle Componenti Indipendenti**: Tecnica che scompone un set di segnali multivariati in componenti additive che si presume siano statisticamente indipendenti. A differenza di PCA, che si concentra sulla massimizzazione della varianza e sull'ortogonalità, ICA cerca di separare le sorgenti sottostanti. È celebre per la sua applicazione nel "problema del cocktail party", dove si separano le voci di diversi interlocutori da un'unica registrazione.

### NMF (Non-Negative Matrix Factorization)

**Fattorizzazione di matrici non negative**: Algoritmo di riduzione della dimensionalità che scompone una matrice di dati in due matrici a valori non negativi. Questa restrizione rende i risultati più facilmente interpretabili, poiché le componenti sono additive e non sottrattive. È particolarmente efficace in domini dove i dati non possono essere negativi, come il conteggio di parole in documenti (topic modeling) o le intensità dei pixel nelle immagini.

### SVD (Singular Value Decomposition)

**Decomposizione ai valori singolari**: Potente tecnica di fattorizzazione di matrici dell'algebra lineare che scompone una matrice in tre matrici distinte (U, Σ, Vᵀ). È la base matematica di molte tecniche, inclusa la PCA. SVD è ampiamente utilizzata per la riduzione della dimensionalità, la compressione di immagini, i sistemi di raccomandazione (collaborative filtering) e la rimozione del rumore dai dati, specialmente quando si lavora con matrici sparse.

---

## Metodi di Ensemble

### Ensemble Methods

**Metodi di insieme (Ensemble Methods)**: Paradigma del machine learning in cui le previsioni di più modelli (chiamati "stimatori di base" o "weak learners") vengono combinate strategicamente per produrre una previsione finale più accurata, stabile e robusta rispetto a quella di un singolo modello. L'idea fondamentale è che "la saggezza della folla" possa superare le prestazioni di un singolo esperto. Le due famiglie principali di metodi di insieme sono il **Bagging**, che mira a ridurre la varianza, e il **Boosting**, che mira a ridurre il bias.

### Bagging

**Bootstrap Aggregating (Bagging)**: Tecnica di insieme che mira a ridurre la varianza di un modello e a migliorarne la stabilità. Il processo si articola in due fasi: 1) **Bootstrap**: Vengono creati numerosi sottoinsiemi del dataset di addestramento originale campionando con reinserimento. 2) **Aggregating**: Un modello di base (es. un albero decisionale) viene addestrato indipendentemente su ciascuno di questi sottoinsiemi. La previsione finale è ottenuta aggregando i risultati di tutti i modelli, tipicamente tramite votazione (classificazione) o media (regressione).

### Boosting

**Potenziamento (Boosting)**: Famiglia di tecniche di insieme che costruisce un modello forte in modo sequenziale e iterativo. A differenza del Bagging, dove i modelli sono indipendenti, nel Boosting ogni nuovo modello viene addestrato per correggere gli errori commessi dai modelli precedenti. Gli esempi che sono stati classificati erroneamente ricevono un peso maggiore, costringendo il modello successivo a concentrarsi su di essi. La previsione finale è una combinazione ponderata delle previsioni di tutti i modelli sequenziali. Il Boosting è molto efficace nel ridurre il bias del modello.

### Random Forest

**Foresta casuale (Random Forest)**: Potente metodo di insieme basato su alberi decisionali che applica la tecnica del Bagging con un'ulteriore fonte di casualità. Oltre a creare ogni albero su un campione bootstrap del training set, durante la costruzione di ogni albero, a ogni suddivisione (nodo), viene considerata solo una selezione casuale di feature. Questo processo di "feature bagging" decorella gli alberi, riducendo ulteriormente la varianza e rendendo il modello finale estremamente robusto all'overfitting. Le previsioni dei singoli alberi vengono poi aggregate tramite votazione di maggioranza (per la classificazione) o media (per la regressione).

### Gradient Boosting

**Gradient Boosting**: Algoritmo di boosting avanzato e molto potente. Invece di modificare i pesi degli esempi come fa AdaBoost, il Gradient Boosting addestra ogni nuovo modello per predire i **residui** (gli errori) del modello precedente. In pratica, ogni albero sequenziale impara a correggere l'errore residuo del "team" di alberi costruiti fino a quel momento. Questo processo è guidato dall'ottimizzazione di una funzione di costo differenziabile tramite discesa del gradiente, rendendolo un metodo flessibile e applicabile a una vasta gamma di problemi (regressione, classificazione).

### AdaBoost

**Adaptive Boosting (AdaBoost)**: Uno dei primi e più famosi algoritmi di boosting. Funziona costruendo un modello forte in modo sequenziale. Ad ogni iterazione, aumenta il peso degli esempi di training che sono stati classificati erroneamente dal modello precedente. In questo modo, i modelli successivi sono costretti a focalizzarsi sui casi più "difficili". La previsione finale è una somma ponderata delle previsioni di tutti i modelli, dove i modelli più accurati ricevono un peso maggiore.

---

## Modelli Lineari

### Linear Regression

**Regressione Lineare (Linear Regression)**: Algoritmo fondamentale di apprendimento supervisionato per problemi di regressione. Il suo obiettivo è modellare la relazione tra una o più feature indipendenti (X) e una variabile target continua (y) trovando la migliore linea (o iperpiano, in più dimensioni) che si adatta ai dati. Questo viene fatto minimizzando la somma dei quadrati delle differenze tra i valori osservati e i valori predetti dal modello (errore quadratico medio). La sua semplicità e interpretabilità lo rendono un ottimo punto di partenza per l'analisi predittiva.

### Logistic Regression

**Regressione Logistica (Logistic Regression)**: Nonostante il nome, è un algoritmo di classificazione, non di regressione. Modella la probabilità che un dato input appartenga a una particolare classe. Utilizza una funzione lineare combinata con la funzione logistica (o sigmoide) per mappare l'output a un valore compreso tra 0 e 1, che viene interpretato come una probabilità. È ampiamente utilizzato per problemi di classificazione binaria (es. sì/no, spam/non-spam) ed è la base per altri algoritmi più complessi.

### Regularization

**Regolarizzazione (Regularization)**: Insieme di tecniche utilizzate per prevenire l'overfitting nei modelli di machine learning, specialmente in quelli lineari. Funziona aggiungendo un termine di penalità alla funzione di costo del modello. Questa penalità scoraggia il modello dall'assegnare pesi (coefficienti) troppo grandi alle feature, costringendolo a trovare una soluzione più semplice e generalizzabile. Le forme più comuni sono la regolarizzazione L1 (Lasso) e L2 (Ridge).

### Lasso Regression (L1)

**Regressione Lasso (L1 Regularization)**: Una versione della regressione lineare che include una penalità di regolarizzazione L1. La penalità è proporzionale alla somma dei valori assoluti dei coefficienti del modello. Una caratteristica chiave di Lasso è la sua capacità di ridurre alcuni coefficienti a esattamente zero. Questo la rende estremamente utile non solo per prevenire l'overfitting, ma anche per eseguire una **selezione automatica delle feature**, eliminando di fatto le variabili meno importanti dal modello.

### Ridge Regression (L2)

**Regressione Ridge (L2 Regularization)**: Una versione della regressione lineare che include una penalità di regolarizzazione L2. La penalità è proporzionale alla somma dei quadrati dei coefficienti. A differenza di Lasso, Ridge tende a ridurre i coefficienti delle feature meno importanti verso lo zero, ma senza mai annullarli completamente. È particolarmente efficace nel gestire la **multicollinearità** (alta correlazione tra feature), poiché distribuisce l'impatto tra le variabili correlate, rendendo il modello più stabile.

### Multicollinearity

**Multicollinearità (Multicollinearity)**: Fenomeno che si verifica quando due o più feature in un modello di regressione sono altamente correlate tra loro. Questo non riduce necessariamente l'accuratezza predittiva del modello nel suo complesso, ma può rendere le stime dei singoli coefficienti molto instabili e difficili da interpretare. In pratica, il modello non riesce a distinguere l'effetto individuale di ciascuna feature correlata sul target. Tecniche come la regressione Ridge o la rimozione di una delle feature correlate possono mitigare il problema.

---

## Support Vector Machines (SVM)

### Support Vectors

**Vettori di supporto (Support Vectors)**: I campioni del dataset di addestramento che si trovano esattamente sul margine o all'interno di esso. Questi punti sono i più difficili da classificare e sono gli unici che influenzano la posizione e l'orientamento dell'iperpiano di separazione. In altre parole, se tutti gli altri punti venissero rimossi, l'iperpiano rimarrebbe invariato. La robustezza e l'efficienza delle SVM derivano dal fatto che la soluzione dipende solo da un sottoinsieme relativamente piccolo di dati di training (i vettori di supporto).

### Hyperplane

**Iperpiano (Hyperplane)**: Il confine di decisione che il modello SVM impara per separare le classi. In uno spazio a due dimensioni (due feature), l'iperpiano è una linea. In tre dimensioni, è un piano. In più di tre dimensioni, è chiamato iperpiano. L'obiettivo di una SVM è trovare l'iperpiano "ottimale", ovvero quello che massimizza la distanza (il margine) tra sé e i punti più vicini di ciascuna classe (i vettori di supporto).

### Margin

**Margine (Margin)**: La distanza tra l'iperpiano di separazione e i vettori di supporto più vicini. Concettualmente, è come una "strada" o una "zona cuscinetto" tra le classi. L'idea centrale delle SVM è massimizzare questo margine. Un margine più ampio implica una maggiore confidenza nella classificazione e porta a un modello con una migliore capacità di generalizzazione, rendendolo meno sensibile a piccole variazioni nei dati di training e più robusto su dati nuovi.

### Kernel Trick

**Trucco del kernel (Kernel Trick)**: Una delle tecniche più potenti e ingegnose delle SVM. Permette all'algoritmo di creare confini di decisione non lineari in modo computazionalmente efficiente. Invece di trasformare esplicitamente i dati in uno spazio a dimensioni molto più elevate (dove potrebbero diventare linearmente separabili), il "trucco" consiste nell'utilizzare una **funzione kernel**. Questa funzione calcola il risultato del prodotto scalare tra i punti come se fossero in quello spazio a dimensione superiore, senza mai eseguire la trasformazione. Questo permette alle SVM di risolvere problemi complessi senza incorrere in costi computazionali proibitivi.

### Tipi di Kernel

Oltre al concetto generico, scikit-learn offre diverse funzioni kernel specifiche, ognuna adatta a diversi tipi di dati e problemi. La scelta del kernel è un iperparametro cruciale. Le più comuni sono:

- **Kernel Lineare (`kernel='linear'`)**: Non applica una vera e propria trasformazione non lineare. Calcola il prodotto scalare nello spazio originale. È veloce e ideale quando i dati sono già (o quasi) linearmente separabili.

- **Kernel Polinomiale (`kernel='poly'`)**: Crea confini di decisione basati su funzioni polinomiali. È utile quando la relazione tra le feature è di natura polinomiale. I suoi iperparametri principali sono `degree` (il grado del polinomio) e `coef0`.

- **Kernel a Base Radiale (RBF) (`kernel='rbf'`)**: Il più popolare e potente. Misura la similarità tra i punti in base alla loro distanza, mappando implicitamente i dati in uno spazio a infinite dimensioni. È estremamente flessibile e spesso la scelta di default. Il suo comportamento è controllato dall'iperparametro `gamma`.

- **Kernel Sigmoide (`kernel='sigmoid'`)**: Basato sulla funzione tangente iperbolica, simile alle funzioni di attivazione usate nelle reti neurali. È meno comune ma può essere utile in specifici contesti.

La scelta del kernel e dei suoi iperparametri (`gamma`, `degree`, `C`) è un passo fondamentale nell'utilizzo delle SVM e viene tipicamente ottimizzata tramite tecniche come la Grid Search.

### RBF Kernel

**Kernel a base radiale (Radial Basis Function Kernel)**: Una delle funzioni kernel più popolari e potenti per le SVM. È un kernel non lineare che funziona misurando la "similarità" tra due punti in base alla loro distanza. Può creare confini di decisione estremamente flessibili e complessi, mappando implicitamente i dati in uno spazio a infinite dimensioni. È spesso la scelta di default quando non si hanno conoscenze a priori sulla distribuzione dei dati. Il suo comportamento è controllato dall'iperparametro `gamma`, che definisce l'influenza di un singolo esempio di training.

### SVR (Support Vector Regression)

**Regressione a vettori di supporto (Support Vector Regression)**: L'adattamento del concetto di SVM ai problemi di regressione. Invece di trovare un iperpiano che massimizza il margine tra le classi, la SVR cerca di adattare un iperpiano che mantenga il maggior numero possibile di punti all'interno di un "tubo" o "margine di tolleranza" definito dall'iperparametro `epsilon`. L'obiettivo è minimizzare l'errore per i punti che cadono al di fuori di questo tubo. I punti che si trovano sul bordo o al di fuori del tubo diventano i vettori di supporto e determinano la funzione di regressione finale.

---

## Metriche di Valutazione

### Accuracy

**Accuratezza (Accuracy)**: La metrica di valutazione più intuitiva per i problemi di classificazione. Misura la proporzione di previsioni corrette sul numero totale di previsioni effettuate. La formula è: `(Veri Positivi + Veri Negativi) / Totale Campioni`. Sebbene sia facile da interpretare, può essere fuorviante in caso di dataset sbilanciati (dove una classe è molto più frequente delle altre). In tali scenari, un modello potrebbe ottenere un'alta accuratezza semplicemente predicendo sempre la classe maggioritaria.

### R² Score

**Coefficiente di determinazione (R² Score)**: Metrica standard per valutare le prestazioni dei modelli di regressione. Indica la proporzione della varianza nella variabile dipendente (target) che è prevedibile dalle variabili indipendenti (feature). Un valore di R² pari a 1.0 indica che il modello spiega perfettamente la variabilità dei dati, mentre un valore di 0 indica che il modello non è migliore di una semplice media. Può assumere anche valori negativi, segnalando che il modello è peggiore della media.

### Mean Squared Error (MSE)

**Errore quadratico medio (Mean Squared Error - MSE)**: Una delle funzioni di costo e metriche di errore più comuni per i problemi di regressione. Calcola la media delle differenze al quadrato tra i valori reali e i valori predetti dal modello. La formula è: `(1/n) * Σ(y_reale - y_predetto)²`. Elevando al quadrato l'errore, questa metrica penalizza maggiormente gli errori più grandi. Poiché l'unità di misura è il quadrato dell'unità originale, spesso si preferisce usare la sua radice quadrata (RMSE - Root Mean Squared Error) per una migliore interpretabilità.

### Cross-validation Score

**Punteggio di validazione incrociata (Cross-validation Score)**: Il risultato ottenuto da una procedura di validazione incrociata. Invece di un singolo punteggio ottenuto da una divisione train-test, la cross-validation produce un insieme di punteggi (uno per ogni fold). Il "cross-validation score" è tipicamente la media di questi punteggi, spesso accompagnata dalla deviazione standard. Questo fornisce una stima molto più robusta e affidabile delle prestazioni del modello, indicando non solo la sua performance media ma anche la sua stabilità.

---

## Concetti Avanzati

### Random State

**Stato casuale (Random State)**: Parametro utilizzato in molti algoritmi e funzioni di scikit-learn (es. `train_test_split`, `RandomForestClassifier`) per inizializzare il generatore di numeri casuali. Impostando `random_state` a un valore intero fisso (es. `random_state=42`), si garantisce che qualsiasi operazione stocastica (come la suddivisione dei dati o l'inizializzazione dei pesi) produca sempre lo stesso risultato. Questo è fondamentale per la **riproducibilità** degli esperimenti, permettendo ad altri di ottenere esattamente i tuoi stessi risultati eseguendo lo stesso codice.

### Learning Rate

**Tasso di apprendimento (Learning Rate)**: Iperparametro cruciale negli algoritmi di ottimizzazione iterativa, come il Gradient Boosting e le reti neurali. Controlla la dimensione del passo che l'algoritmo compie per aggiornare i parametri del modello in direzione opposta al gradiente della funzione di costo. Un `learning_rate` troppo alto può far sì che l'algoritmo "salti" il minimo ottimale, non riuscendo a convergere. Un `learning_rate` troppo basso può rendere l'addestramento eccessivamente lento o bloccarlo in un minimo locale.

### N_estimators

**Numero di stimatori (N_estimators)**: Iperparametro comune nei metodi di insieme come Random Forest e Gradient Boosting. Definisce il numero di modelli di base (tipicamente alberi decisionali) che verranno costruiti e combinati nell'ensemble. Un numero maggiore di `n_estimators` generalmente migliora le prestazioni e la robustezza del modello, ma aumenta anche il tempo di calcolo e l'utilizzo della memoria. Oltre un certo punto, i benefici diventano marginali, quindi è importante trovare un buon compromesso.

### Alpha

**Parametro di regolarizzazione (Alpha)**: Iperparametro che controlla l'intensità della penalità di regolarizzazione nei modelli lineari come Ridge (L2) e Lasso (L1). Un valore di `alpha` più alto aumenta la forza della regolarizzazione, costringendo i coefficienti del modello a ridursi. Questo aiuta a prevenire l'overfitting ma, se troppo alto, può portare a un underfitting (modello troppo semplice). Un `alpha` pari a 0 rimuove completamente la regolarizzazione. La scelta ottimale di `alpha` è tipicamente effettuata tramite cross-validation.

### Epsilon

**Margine di tolleranza (Epsilon)**: Iperparametro specifico della Support Vector Regression (SVR). Definisce la larghezza del "tubo" o "margine" attorno alla funzione di regressione. I punti che cadono all'interno di questo tubo non contribuiscono all'errore di addestramento. Solo i punti che si trovano al di fuori del margine di tolleranza vengono penalizzati. Un `epsilon` più grande permette a più punti di essere considerati "corretti", risultando in un modello più semplice e potenzialmente meno sensibile al rumore.

### Feature Selection

**Selezione delle feature (Feature Selection)**: Processo strategico di selezione di un sottoinsieme delle feature più rilevanti da un dataset. Gli obiettivi sono semplificare il modello, ridurre i tempi di addestramento, mitigare la maledizione della dimensionalità e, in alcuni casi, migliorare le prestazioni del modello eliminando il rumore. Le tecniche includono metodi a filtro (basati su test statistici), metodi wrapper (che usano un modello per valutare i sottoinsiemi di feature) e metodi embedded (come la regressione Lasso, che esegue la selezione durante l'addestramento).

### Generalization

**Generalizzazione (Generalization)**: L'obiettivo finale del machine learning supervisionato. Rappresenta la capacità di un modello, addestrato su un set di dati specifico, di fare previsioni accurate su dati nuovi e mai visti prima che provengono dalla stessa distribuzione. Un modello con una buona generalizzazione ha appreso i pattern sottostanti e non il rumore specifico dei dati di training. L'overfitting è il principale ostacolo alla generalizzazione. Le prestazioni del modello sul test set sono la misura principale della sua capacità di generalizzazione.
