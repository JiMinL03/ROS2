// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_interface:msg/StartCar.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__TRAITS_HPP_
#define CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__TRAITS_HPP_

#include "custom_interface/msg/detail/start_car__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<custom_interface::msg::StartCar>()
{
  return "custom_interface::msg::StartCar";
}

template<>
inline const char * name<custom_interface::msg::StartCar>()
{
  return "custom_interface/msg/StartCar";
}

template<>
struct has_fixed_size<custom_interface::msg::StartCar>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<custom_interface::msg::StartCar>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<custom_interface::msg::StartCar>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__TRAITS_HPP_
