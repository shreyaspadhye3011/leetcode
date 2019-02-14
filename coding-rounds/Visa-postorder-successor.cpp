// CPP program to find postorder successor of 
// given node. 
#include <iostream> 
using namespace std; 
   
struct Node { 
    struct Node *left, *right, *parent; 
    int value; 
}; 
   
// Utility function to create a new node with 
// given value. 
struct Node* newNode(int value) 
{ 
    Node* temp = new Node; 
    temp->left = temp->right = temp->parent = NULL;
    temp->value = value; 
    return temp; 
} 
   
Node* postorderSuccessor(Node* root, Node* n) 
{ 
    // Root has no successor in postorder 
    // traversal 
    if (n == root) 
        return NULL; 
   
    // If given node is right child of its 
    // parent or parent's right is empty, then  
    // parent is postorder successor. 
    Node* parent = n->parent; 
    if (parent->right == NULL || parent->right == n) 
        return parent; 
   
    // In all other cases, find the leftmost  
    // child in left substree of parent. 
    Node* curr = parent->right; 
    while (curr->left != NULL) 
        curr = curr->left; 
   
    return curr; 
} 
   
// Driver code 
int main() 
{ 
    struct Node* root = newNode(20); 
    root->parent = NULL; 
    root->left = newNode(10); 
    root->left->parent = root; 
    root->left->left = newNode(4); 
    root->left->left->parent = root->left; 
    root->left->right = newNode(18); 
    root->left->right->parent = root->left; 
    root->right = newNode(26); 
    root->right->parent = root; 
    root->right->left = newNode(24); 
    root->right->left->parent = root->right; 
    root->right->right = newNode(27); 
    root->right->right->parent = root->right; 
    root->left->right->left = newNode(14); 
    root->left->right->left->parent = root->left->right; 
    root->left->right->left->left = newNode(13); 
    root->left->right->left->left->parent = root->left->right->left; 
    root->left->right->left->right = newNode(15); 
    root->left->right->left->right->parent = root->left->right->left; 
    root->left->right->right = newNode(19); 
    root->left->right->right->parent = root->left->right; 
   
    struct Node* res = postorderSuccessor(root, root->left->right->right); 
    if (res)  
        printf("Postorder successor of %d is %d\n", 
               root->left->right->right->value, res->value);     
    else
        printf("Postorder successor of %d is NULL\n", 
               root->left->right->right->value);     
   
    return 0; 
}