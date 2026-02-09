import sqlite3

from tkinter import messagebox


class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect("estudante.db")
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute(
            """
        CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        tel TEXT NOT NULL,
                        sexo TEXT NOT NULL,
                        data_nascimento TEXT NOT NULL,
                        endereco TEXT NOT NULL,
                        curso TEXT NOT NULL,
                        picture TEXT NOT NULL
                        )
                    """
        )

    def register_students(self, students):
        self.c.execute(
            "INSERT INTO students (nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?,?,?,?,?,?,?,?)",
            (students),
        )
        self.conn.commit()

        messagebox.showinfo("Sucesso", "Registro com sucesso")

    def view_all_students(self):
        self.c.execute("SELECT * FROM students")
        dados = self.c.fetchall()

        for i in dados:
            print(
                f"""ID:{i[0]}, | Nome: {i[1]}, | Email: {i[2]}, | Tel: {i[3]}, | Sexo: {i[4]}, | Data_nascimento: {i[5]}, | Endereco: {i[6]}, | Curso: {i[7]}, | Picture: {i[8]}
                -----------------------------------------------------------------------------"""
            )

    def search_students(self, id):
        self.c.execute("SELECT * FROM students WHERE id = ?", (id,))
        dados = self.c.fetchone()
        print(
            f"""ID:{dados[0]}, | Nome: {dados[1]}, | Email: {dados[2]}, | Tel: {dados[3]}, | Sexo: {dados[4]}, |
         Data_nascimento: {dados[5]}, | Endereco: {dados[6]}, | Curso: {dados[7]}, | Picture: {dados[8]}"""
        )

    def update_students(self, new_value):
        query = """
                UPDATE students SET 
                    nome = ?,
                    email = ?,
                    tel = ?,
                    sexo = ?,
                    data_nascimento = ?,
                    endereco = ?,
                    curso = ?,
                    picture = ?        
                WHERE id = ?
                """
        self.c.execute(query, new_value)
        self.conn.commit()
        messagebox.showinfo(
            "Sucesso," f"Estudante com ID:{new_value[8]} foi atualizado!"
        )

    def delete_students(self, id):
        self.c.execute("DELETE FROM students WHERE id = ?", (id,))
        self.conn.commit()
        messagebox.showinfo("Sucesso", f"Usuário {id} deletado com sucesso")

        # Instancia do sistema


# system_register = SistemaDeRegistro()

# ________________________________________________________________________#


# Visualizar Estudantes


# show_students = system_register.view_all_students()


# ________________________________________________________________________#

# Visualizar Estudante Único

# view_student = system_register.search_students()

# ________________________________________________________________________#

# Cadastro Estudante

# estudante1 = ('Julia', 'Julia@gmail.com', '4848484848448', 'Masculino', '12/12/2000', 'Rua Julia', 'Curso Julia', 'Picture.jpg')
# system_register.register_students(estudante1)
# show_students = system_register.view_all_students()
# ________________________________________________________________________#


# Atualizar Estudante

# estudante1 = ('Teste1', 'teste1@gmail.com', '4444', 'Masculino', '12/12/1212', 'Rua Teste', 'Curso teste', 'Picture.png', 2)

# att_student = system_register.update_students(estudante1)

# ________________________________________________________________________#

# Deletar Estudante

# del_student = system_register.delete_students(2)

# ________________________________________________________________________#
