from tree import BinarySearchTree,BinaryTree,Node

class Record:
    def __init__(self, cpf, name, birthdate):
        self.cpf = cpf
        self.name = name
        self.birthdate = birthdate

class EDL:
    def __init__(self) -> None:
        self.edl = []
    # função para inserir um registro com complexidade O(1)
    def insert_record(self,record):
        self.edl.append(record)

    # função que deleta um resgistro da EDL
    def delete_record(self,cpf):
        for record in self.edl:
            if record.cpf == cpf:
                record.cpf = ''  # marca a deleção

    # função para recuperar um rsegistro pelo seu índice
    def get_record_by_index(self,index):
        if 0 <= index < len(self.edl):
            return self.edl[index]
        return None
