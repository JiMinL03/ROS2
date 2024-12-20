// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from custom_interface:msg/StartCar.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__STRUCT_HPP_
#define CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__custom_interface__msg__StartCar __attribute__((deprecated))
#else
# define DEPRECATED__custom_interface__msg__StartCar __declspec(deprecated)
#endif

namespace custom_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct StartCar_
{
  using Type = StartCar_<ContainerAllocator>;

  explicit StartCar_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->car = "";
    }
  }

  explicit StartCar_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : car(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->car = "";
    }
  }

  // field types and members
  using _car_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _car_type car;

  // setters for named parameter idiom
  Type & set__car(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->car = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_interface::msg::StartCar_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_interface::msg::StartCar_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_interface::msg::StartCar_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_interface::msg::StartCar_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_interface::msg::StartCar_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_interface::msg::StartCar_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_interface::msg::StartCar_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_interface::msg::StartCar_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_interface::msg::StartCar_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_interface::msg::StartCar_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_interface__msg__StartCar
    std::shared_ptr<custom_interface::msg::StartCar_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_interface__msg__StartCar
    std::shared_ptr<custom_interface::msg::StartCar_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StartCar_ & other) const
  {
    if (this->car != other.car) {
      return false;
    }
    return true;
  }
  bool operator!=(const StartCar_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StartCar_

// alias to use template instance with default allocator
using StartCar =
  custom_interface::msg::StartCar_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace custom_interface

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__START_CAR__STRUCT_HPP_
