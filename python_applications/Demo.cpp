#include<iostream>
using namespace std;

typedef struct node
{
    int data;
    struct node *next;
    struct node *prev;
}NODE,*PNODE;

class DoublyLL
{
    private:
        PNODE First;
        int iCount;

    public:
        DoublyLL();

        void Display();
        int Count();

        void InsertFirst(int No);
        void InsertLast(int No);        
        void InsertAtPos(int No, int iPos);

        void DeleteFirst();
        void DeleteLast();
        void DeleteAtPos(int iPos);
};

DoublyLL::DoublyLL()
{
    this->iCount = 0;
    this->First = NULL;
}

void DoublyLL::InsertFirst(int No)
{
    PNODE newn = NULL;
    newn = new NODE;

    newn->data = No;
    newn->next = NULL;
    newn->prev = NULL;

    if (First == NULL)
    {
        First = newn;
    }
    else
    {
        newn->next = First;
        First->prev = newn;
        First = newn;
    }   
}

void DoublyLL::InsertLast(int No)
{
    PNODE newn = NULL;
    PNODE temp = First;

    newn = new NODE;

    newn->data = No;
    newn->next = NULL;
    newn->prev = NULL;

    if (First == NULL)
    {
        First = newn;
    }
    else
    {
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp ->next = newn;
        newn->prev = temp;
    }   
}

void DoublyLL::Display()
{
    PNODE temp = First;

    while (temp != NULL)
    {
        cout<<"| "<<temp->data<<"|-> ";
        temp = temp->next;
    }
    
}

int DoublyLL::Count()
{
    return 0;
}

void DoublyLL::InsertAtPos(int No, int iPos)
{}

void DoublyLL::DeleteFirst()
{

    if (First == NULL)
    {
        cout<<"LL is emptya \n";
        return;
    }
    else if(First->next == NULL)
    {
        delete First;
        First = NULL;
    }
    else
    {
        First = First->next;
        delete First->prev;
        First->prev = NULL;
    }
    
}

void DoublyLL::DeleteLast()
{}

void DoublyLL::DeleteAtPos(int iPos)
{}

int main()
{
    DoublyLL obj;    

    obj.InsertFirst(11);
    obj.InsertFirst(21);
    obj.InsertFirst(51);
    obj.InsertLast(61);
    obj.InsertLast(61);
    obj.InsertLast(61);
    obj.InsertLast(61);
    //obj.DeleteFirst();
    obj.Display();

    return 0;
}