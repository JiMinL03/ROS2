// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_interface:msg/StartCar.idl
// generated code does not contain a copyright notice
#include "custom_interface/msg/detail/start_car__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `car`
#include "rosidl_runtime_c/string_functions.h"

bool
custom_interface__msg__StartCar__init(custom_interface__msg__StartCar * msg)
{
  if (!msg) {
    return false;
  }
  // car
  if (!rosidl_runtime_c__String__init(&msg->car)) {
    custom_interface__msg__StartCar__fini(msg);
    return false;
  }
  return true;
}

void
custom_interface__msg__StartCar__fini(custom_interface__msg__StartCar * msg)
{
  if (!msg) {
    return;
  }
  // car
  rosidl_runtime_c__String__fini(&msg->car);
}

custom_interface__msg__StartCar *
custom_interface__msg__StartCar__create()
{
  custom_interface__msg__StartCar * msg = (custom_interface__msg__StartCar *)malloc(sizeof(custom_interface__msg__StartCar));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_interface__msg__StartCar));
  bool success = custom_interface__msg__StartCar__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
custom_interface__msg__StartCar__destroy(custom_interface__msg__StartCar * msg)
{
  if (msg) {
    custom_interface__msg__StartCar__fini(msg);
  }
  free(msg);
}


bool
custom_interface__msg__StartCar__Sequence__init(custom_interface__msg__StartCar__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  custom_interface__msg__StartCar * data = NULL;
  if (size) {
    data = (custom_interface__msg__StartCar *)calloc(size, sizeof(custom_interface__msg__StartCar));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_interface__msg__StartCar__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_interface__msg__StartCar__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
custom_interface__msg__StartCar__Sequence__fini(custom_interface__msg__StartCar__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_interface__msg__StartCar__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

custom_interface__msg__StartCar__Sequence *
custom_interface__msg__StartCar__Sequence__create(size_t size)
{
  custom_interface__msg__StartCar__Sequence * array = (custom_interface__msg__StartCar__Sequence *)malloc(sizeof(custom_interface__msg__StartCar__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = custom_interface__msg__StartCar__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
custom_interface__msg__StartCar__Sequence__destroy(custom_interface__msg__StartCar__Sequence * array)
{
  if (array) {
    custom_interface__msg__StartCar__Sequence__fini(array);
  }
  free(array);
}
