import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Teste n8n")
    root.geometry("500x250")
    root.configure(bg="#1e1e2e")

    tk.Label(root, text="Projeto de Teste n8n", font=("Arial", 22, "bold"),
             fg="#ff6d5a", bg="#1e1e2e").pack(pady=(50, 10))
    tk.Label(root, text="Este projeto será usado para testar a automação no n8n.",
             font=("Arial", 11), fg="white", bg="#1e1e2e").pack()

    root.mainloop()


if __name__ == "__main__":
    main()
