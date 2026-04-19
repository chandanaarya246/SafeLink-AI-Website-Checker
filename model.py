def check_url(url):
    suspicious_words = ["login", "verify", "bank", "update", "free", "gift"]

    score = 0
    for word in suspicious_words:
        if word in url.lower():
            score += 1

    if score >= 2:
        return "Dangerous Website ⚠️"
    elif score == 1:
        return "Suspicious Website ⚡"
    else:
        return "Safe Website ✅"
