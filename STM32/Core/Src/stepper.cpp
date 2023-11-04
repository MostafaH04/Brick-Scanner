#include <stepper.hpp>

//Pin struct
Pin::Pin(GPIO_TypeDef *GPIOx, uint16_t GPIO_Pin) : pin_register(GPIOx), pin_number(GPIO_Pin) {

}

void Pin::write_pin(GPIO_PinState PinState) {
	HAL_GPIO_WritePin(pin_register, pin_number, PinState);
}

GPIO_PinState Pin::read_pin() {
	return 	HAL_GPIO_ReadPin(pin_register, pin_number);
}

//Stepper struct
Stepper::Stepper(Pin *step, Pin *direction) : step_pin(step), direction_pin(direction) {

}

void Stepper::rotate_angle(float angle, bool clockwise) {
	direction_pin.write_pin((clockwise == true) ? HIGH : LOW);

	uint8_t steps = angle / STEP_ANGLE;

	for(uint8_t step = 0; step < steps; step++) {
		step_pin.write_pin(HIGH);
		HAL_delay(1);
		step_pin.write_pin(LOW);
		HAL_delay(1);
	}
}

