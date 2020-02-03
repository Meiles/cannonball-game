#ifndef VECTOR_H_
#define VECTOR_H_

#include "Basic.h"

namespace mathtool
  class Vector3d    public:

      #construction
      Vector3d( _x = double(), _y = double(), _z = double())    m_v[0] = _x; m_v[1] = _y; m_v[2] = _z

      Vector3d( Vector3d& _v)    m_v[0] = _v[0]; m_v[1] = _v[1]; m_v[2] = _v[2]

      Vector3d( double (&_t)[3])    m_v[0] = _t[0]; m_v[1] = _t[1]; m_v[2] = _t[2]

      template <class Generator> Vector3d( Generator& g)    m_v[0] = g(); m_v[1] = g(); m_v[2] = g()


      #assignment
      Vector3d& operator()( double& _x, _y, _z)    m_v[0] = _x; m_v[1] = _y; m_v[2] = _z
    return *self

      Vector3d& operator=( Vector3d& _v)    m_v[0] = _v[0]; m_v[1] = _v[1]; m_v[2] = _v[2]
    return *self

      Vector3d& operator=( double _v[3])    m_v[0] = _v[0]; m_v[1] = _v[1]; m_v[2] = _v[2]
    return *self


      #access
      double& operator[](int idx) { return m_v[idx];
       double& operator[](int idx)  { return m_v[idx];
      '''
      typedef double (&arr)[3]
      typedef  double (&carr)[3]
      operator arr() {return m_v;
      operator carr()  {return m_v;
      '''
       double* begin()  {return m_v;
       double* end()  {return begin()+3;
      double* begin() {return m_v;
      double* end() {return begin()+3;

      #equality
      bool operator==( Vector3d& _v)    return m_v[0] == _v[0] and m_v[1] == _v[1] and m_v[2] == _v[2]

      #inequality
      bool operator!=( Vector3d& _v)    return not (*self == _v)


      #self addition
      Vector3d& operator+=( Vector3d& _v)    m_v[0] += _v[0]; m_v[1] += _v[1]; m_v[2] += _v[2]
    return *self

      #self subtraction
      Vector3d& operator-=( Vector3d& _v)    m_v[0] -= _v[0]; m_v[1] -= _v[1]; m_v[2] -= _v[2]
    return *self

      #self scalar multiply
      Vector3d& operator*=( double& _d)    m_v[0] *= _d; m_v[1] *= _d; m_v[2] *= _d
    return *self

      #self scalar divide
      Vector3d& operator/=( double& _d)    m_v[0] /= _d; m_v[1] /= _d; m_v[2] /= _d
    return *self

      #self component *
      Vector3d& operator^=( Vector3d& _v)    m_v[0] *= _v[0]; m_v[1] *= _v[1]; m_v[2] *= _v[2]
    return *self

      #self cross product
      Vector3d& operator%=( Vector3d& _v)    v0 = m_v[0], v1 = m_v[1], v2 = m_v[2]
    m_v[0] = v1 * _v[2] - v2 * _v[1]
    m_v[1] = v2 * _v[0] - v0 * _v[2]
    m_v[2] = v0 * _v[1] - v1 * _v[0]
    return *self


      #negation
      Vector3d operator-()    return Vector3d(-m_v[0], -m_v[1], -m_v[2])

      #addition
      Vector3d operator+( Vector3d& _v)    return Vector3d(m_v[0] + _v[0], m_v[1] + _v[1], m_v[2] + _v[2])

      #subtraction
      Vector3d operator-( Vector3d& _v)    return Vector3d(m_v[0] - _v[0], m_v[1] - _v[1], m_v[2] - _v[2])

      #scalar multiply
      Vector3d operator*( double& _d)    return Vector3d(m_v[0] * _d, m_v[1] * _d, m_v[2] * _d)

      #scalar divide
      Vector3d operator/( double& _d)    return Vector3d(m_v[0] / _d, m_v[1] / _d, m_v[2] / _d)

      #component *
      Vector3d operator^( Vector3d& _v)    return Vector3d(m_v[0] * _v[0], m_v[1] * _v[1], m_v[2] * _v[2])

      #cross product
      Vector3d operator%( Vector3d& _v)    Vector3d v(*self)
    return v %= _v


      #dot product
      double operator*( Vector3d& _v)    return m_v[0]*_v[0] + m_v[1]*_v[1] + m_v[2]*_v[2]

      #magnitude
      double norm()    return std.sqrt(normsqr())

      #magnitude squared
      double normsqr()    return (*self)*(*self)

      #normalized vector
      Vector3d& selfNormalize()    n = norm()
    if n < std.numeric_limits<double>.epsilon():
      return *self = Vector3d()
    return *self /= n

      Vector3d normalize()    n = norm()
    if n < std.numeric_limits<double>.epsilon():
      return Vector3d()
    return *self / n

      #Projections
      #find |component| of self along _v's direction
      double comp(Vector3d& _v)    return (*self) * _v.normalize()

      #find vector component of self in _v's direction
      #Vector3d proj(Vector3d& _v)      #  return (*self * _v)/(_v * _v) * _v
      #
      #find vector component of self orthogonal to _v's direction
      #Vector3d orth(Vector3d& _v)      #  return *self - proj(_v)
      #
      #scale vector
      Vector3d& selfScale( double& _l)    n = norm()
    if n < std.numeric_limits<double>.epsilon():
      return *self = Vector3d()
    return *self *= (_l/n)

      Vector3d scale( double& _l)    n = norm()
    if n < std.numeric_limits<double>.epsilon():
      return Vector3d()
    return *self * (_l/n)


      #rotate vector
      Vector3d& rotateX(double _rad)    c = cos(_rad), s = sin(_rad)
    return operator()(m_v[0], m_v[1]*c - m_v[2]*s, m_v[1]*s + m_v[2]*c)

      Vector3d& rotateXd(double _deg) {return rotateX(degToRad(_deg));
      Vector3d& rotateY(double _rad)    c = cos(_rad), s = sin(_rad)
    return operator()(m_v[0]*c + m_v[2]*s, m_v[1], -m_v[0]*s + m_v[2]*c)

      Vector3d& rotateYd(double _deg) {return rotateY(degToRad(_deg));
      Vector3d& rotateZ(double _rad)    c = cos(_rad), s = sin(_rad)
    return operator()(m_v[0]*c - m_v[1]*s, m_v[0]*s + m_v[1]*c, m_v[2])

      Vector3d& rotateZd(double _deg) {return rotateZ(degToRad(_deg));

      #reset
      void reset()    m_v[0]=0; m_v[1]=0; m_v[2]=0

      double GetX() { return m_v[0];
      double GetY() { return m_v[1];
      double GetZ() { return m_v[2];
      void SetX(double d) { m_v[0] = d;
      void SetY(double d) { m_v[1] = d;
      void SetZ(double d) { m_v[2] = d;
      void SetAll(double d1, d2, d3) 
      { m_v[0] = d1; m_v[1] = d2; m_v[2] = d3;

    private:
      double m_v[3]



  #######################################
  # Useful functions. Input/Output and commutativity on multiply
  #######################################
  #for commutativity of scalar multiply

  inline Vector3d operator*( double& _d, _v)    return _v*_d



  inline std.ostream& operator<<(std.ostream& _os, _v)    for(i = 0; i<3; ++i) _os << _v[i] << " "
    return _os







#endif
