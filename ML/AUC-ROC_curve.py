# Manually computing AUC-ROC using trapezoidal rule integration
truth_labels = [1, 0, 1, 0, 1]
predicted_probs = [0.9, 0.6, 0.8, 0.2, 0.5]

def compute_aucroc(truth, predicted):
    tprs, fprs = [], []
    thresholds = [1, 0.8, 0.6, 0.4, 0.2, 0]
    for threshold in thresholds:
        tp = fp = tn = fn = 0
        for t, p in zip(truth, predicted):
            if p >= threshold:
                if t == 1:
                    tp += 1
                else:
                    fp += 1
            else:
                if t == 1:
                    fn += 1
                else:
                    tn += 1
        tprs.append(tp / (tp + fn) if (tp + fn) > 0 else 0)
        fprs.append(fp / (tn + fp) if (tn + fp) > 0 else 1)
    aucroc = sum(0.5 * (fprs[i] - fprs[i - 1]) * (tprs[i] + tprs[i - 1]) for i in range(1, len(fprs)))
    return aucroc

# Calculate and print the AUC-ROC value
aucroc_value = compute_aucroc(truth_labels, predicted_probs)
print(f"The AUC-ROC value is: {aucroc_value:.2f}")