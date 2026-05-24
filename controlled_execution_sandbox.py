def analyze_input(cmd):
    # categorize threats
    threats = {
        "system access": ["os", "sys", "subprocess"],
        "file access": ["open", "read", "write"],
        "code execution": ["exec", "eval", "__"],
        "network": ["socket"]
    }

    for category, keywords in threats.items():
        for word in keywords:
            if word in cmd:
                return category

    return None


def safe_execute(cmd):
    # basic length control
    if len(cmd) > 50:
        return "❌ Blocked: input too long"

    # detect type of attack
    threat_type = analyze_input(cmd)

    if threat_type:
        return f"❌ Blocked: {threat_type} attempt detected"

    try:
        # restricted execution
        result = eval(cmd, {"__builtins__": None}, {})
        return f"✅ Output: {result}"

    except:
        return "⚠️ Invalid or not allowed"


# -------- MAIN --------
def main():
    print("=== Controlled Execution Sandbox ===")
    print("Type 'exit' to stop\n")

    history = []  # log attempts

    while True:
        cmd = input(">>> ")

        if cmd.lower() == "exit":
            print("\nSession Summary:")
            for h in history:
                print("-", h)
            break

        result = safe_execute(cmd)
        print(result)

        # store history
        history.append(f"{cmd} → {result}")


if __name__ == "__main__":
    main()