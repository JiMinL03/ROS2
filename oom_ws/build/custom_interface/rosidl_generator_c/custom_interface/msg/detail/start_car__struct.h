// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interface:msg/StartCar.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__STRUCT_H_
#define CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'car'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/StartCar in the package custom_interface.
typedef struct custom_interface__msg__StartCar
{
  rosidl_runtime_c__String car;
} custom_interface__msg__StartCar;

// Struct for a sequence of custom_interface__msg__StartCar.
typedef struct custom_interface__msg__StartCar__Sequence
{
  custom_interface__msg__StartCar * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interface__msg__StartCar__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__STRUCT_H_
