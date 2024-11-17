// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from custom_interface:msg/StartCar.idl
// generated code does not contain a copyright notice
#include "custom_interface/msg/detail/start_car__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "custom_interface/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "custom_interface/msg/detail/start_car__struct.h"
#include "custom_interface/msg/detail/start_car__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // car
#include "rosidl_runtime_c/string_functions.h"  // car

// forward declare type support functions


using _StartCar__ros_msg_type = custom_interface__msg__StartCar;

static bool _StartCar__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _StartCar__ros_msg_type * ros_message = static_cast<const _StartCar__ros_msg_type *>(untyped_ros_message);
  // Field name: car
  {
    const rosidl_runtime_c__String * str = &ros_message->car;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _StartCar__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _StartCar__ros_msg_type * ros_message = static_cast<_StartCar__ros_msg_type *>(untyped_ros_message);
  // Field name: car
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->car.data) {
      rosidl_runtime_c__String__init(&ros_message->car);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->car,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'car'\n");
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_interface
size_t get_serialized_size_custom_interface__msg__StartCar(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _StartCar__ros_msg_type * ros_message = static_cast<const _StartCar__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name car
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->car.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _StartCar__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_custom_interface__msg__StartCar(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_interface
size_t max_serialized_size_custom_interface__msg__StartCar(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: car
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _StartCar__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_custom_interface__msg__StartCar(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_StartCar = {
  "custom_interface::msg",
  "StartCar",
  _StartCar__cdr_serialize,
  _StartCar__cdr_deserialize,
  _StartCar__get_serialized_size,
  _StartCar__max_serialized_size
};

static rosidl_message_type_support_t _StartCar__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_StartCar,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, custom_interface, msg, StartCar)() {
  return &_StartCar__type_support;
}

#if defined(__cplusplus)
}
#endif
