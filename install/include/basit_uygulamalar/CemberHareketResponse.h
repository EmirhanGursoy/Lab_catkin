// Generated by gencpp from file basit_uygulamalar/CemberHareketResponse.msg
// DO NOT EDIT!


#ifndef BASIT_UYGULAMALAR_MESSAGE_CEMBERHAREKETRESPONSE_H
#define BASIT_UYGULAMALAR_MESSAGE_CEMBERHAREKETRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace basit_uygulamalar
{
template <class ContainerAllocator>
struct CemberHareketResponse_
{
  typedef CemberHareketResponse_<ContainerAllocator> Type;

  CemberHareketResponse_()
    {
    }
  CemberHareketResponse_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> const> ConstPtr;

}; // struct CemberHareketResponse_

typedef ::basit_uygulamalar::CemberHareketResponse_<std::allocator<void> > CemberHareketResponse;

typedef boost::shared_ptr< ::basit_uygulamalar::CemberHareketResponse > CemberHareketResponsePtr;
typedef boost::shared_ptr< ::basit_uygulamalar::CemberHareketResponse const> CemberHareketResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace basit_uygulamalar

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "basit_uygulamalar/CemberHareketResponse";
  }

  static const char* value(const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
"\n"
;
  }

  static const char* value(const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CemberHareketResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // BASIT_UYGULAMALAR_MESSAGE_CEMBERHAREKETRESPONSE_H
