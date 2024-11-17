// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interface:msg/StartCar.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__BUILDER_HPP_
#define CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__BUILDER_HPP_

#include "custom_interface/msg/detail/start_car__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_interface
{

namespace msg
{

namespace builder
{

class Init_StartCar_car
{
public:
  Init_StartCar_car()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interface::msg::StartCar car(::custom_interface::msg::StartCar::_car_type arg)
  {
    msg_.car = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interface::msg::StartCar msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interface::msg::StartCar>()
{
  return custom_interface::msg::builder::Init_StartCar_car();
}

}  // namespace custom_interface

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__BUILDER_HPP_
