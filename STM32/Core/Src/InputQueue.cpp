#include <input_queue.hpp>
//Constructor

Data:: Data(): base_angle(0), base_angle_dir(false), arm_angle(0), arm_angle_dir(false)  {} ;
Data:: Data(float base_angle, bool base_angle_dir, float arm_angle, bool arm_angle_dir): base_angle(base_angle), base_angle_dir( base_angle_dir), arm_angle(arm_angle),  arm_angle_dir( arm_angle_dir) {};

//Constructor
Input_Queue:: Input_Queue(): front(nullptr), rear(nullptr) {}


//Destructor
Input_Queue:: ~Input_Queue(){
	while(!isEmpty()){
		dequeue();
	}
}

bool Input_Queue:: isEmpty(){
	return front == nullptr;

}

//Push
void Input_Queue:: enqueue(Data data){
	Node*  newNode = new Node{data ,nullptr};
	if(isEmpty()){
		front = newNode;
		rear = newNode;
	}else{
		rear-> next = newNode;
		rear = newNode;
	}
}


//Pop

Data Input_Queue:: dequeue(){
	if(!isEmpty()){
		Data data = front->data;
		Node* temp = front;
		front = front->next;
		delete temp;

		if(front==nullptr){
			rear = nullptr;
		}
	return data;
	}
}


