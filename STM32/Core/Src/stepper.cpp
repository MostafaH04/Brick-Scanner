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
Stepper::Stepper(Pin *step, Pin *direction, uint8_t resolution) : step_pin(step), direction_pin(direction), step_res(resolution) {

}

void Stepper::rotate_angle(float angle, bool clockwise, uint8_t rpm) {
	direction_pin -> write_pin((clockwise == true) ? HIGH : LOW);

	uint16_t steps = (angle / STEP_ANGLE) * (step_res);

	uint32_t us_per_step = (1 / rpm) * (60000000) * (1 / (200 * step_res));

	for(uint16_t step = 0; step < steps; step++) {
		step_pin -> write_pin(HIGH);
		delay_us(us_per_step / 2);
		step_pin -> write_pin(LOW);
		delay_us(us_per_step / 2);
	}
}

void Stepper::update_res(int resolution) {
	step_res = resolution;
}
