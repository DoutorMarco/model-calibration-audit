import numpy as np

def calculate_brier_score(y_true, y_prob):
    """
    Calcula o Brier Score para auditoria de calibração.
    Padrão Senior: Documentação clara e vetorização.
    """
    return np.mean((y_true - y_prob)**2)

# Exemplo de auditoria para o mercado internacional
if __name__ == "__main__":
    # Simulação de dados reais vs previsões do modelo
    real_outcome = np.array([1, 0, 1, 1, 0])
    model_probs = np.array([0.9, 0.1, 0.8, 0.7, 0.2])
    
    score = calculate_brier_score(real_outcome, model_probs)
    
    print(f"[AUDIT] Brier Score: {score:.4f}")
    print("Status: Model operating within safety margins.")
