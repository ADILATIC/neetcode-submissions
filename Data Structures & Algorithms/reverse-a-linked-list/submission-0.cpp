/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* temp = nullptr;

        if(head == nullptr){
            return nullptr;
        }

        while(curr != nullptr){  //Gets us to the end of the LL
            temp = curr->next;              //Stores the next into temp
            curr->next = prev;              // Store prev into the curr next
            prev = curr;                //Stores into the prev
            curr = temp ;         //iterates the curr 
        }
        //prev = curr;
        return prev;
    }
};
