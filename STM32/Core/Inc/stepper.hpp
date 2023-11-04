#ifndef INC_STEPPER_HPP
#define INC_STEPPER_HPP_

#include <main.hpp>

#define HIGH GPIO_PIN_SET
#define LOW GPIO_PIN_RESET
#define STEP_ANGLE 1.8

struct Pin {
	GPIO_TypeDef *pin_register;
	uint16_t pin_number;

	Pin(GPIO_TypeDef *GPIOx, uint16_t GPIO_Pin);
	void write_pin(GPIO_PinState PinState);
	GPIO_PinState read_pin();
};

class Stepper {
private:
	Pin *step_pin;
	Pin *direction_pin;

public:
	Stepper(Pin *step, Pin *direction);
	void rotate_angle(float angle, bool clockwise, uint8_t rpm);
};

#endif /* INC_STEPPER_HPP_ */
