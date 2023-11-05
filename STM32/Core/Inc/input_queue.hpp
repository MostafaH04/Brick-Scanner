#ifndef INC_INPUT_QUEUE_HPP
#define INC_INPUT_QUEUE_HPP_

#include <main.hpp>
struct Data {
	float base_angle;
	bool base_angle_dir;
	float arm_angle;
	bool arm_angle_dir;
	Data();
	Data(float base_angle, bool base_angle_dir, float arm_angle, bool arm_angle_dir );
};
class Input_Queue {
private:
	struct Node{
		Data data;
		struct Node* next;
	};
	Node* front;
	Node* rear;
public:
Input_Queue();
~Input_Queue();
void enqueue(Data data);
Data dequeue();
bool isEmpty();
};
	

#endif /* INC_INPUT_QUEUE_HPP_ */
