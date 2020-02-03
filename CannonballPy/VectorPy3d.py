#ifndef VECTOR_H_
#define VECTOR_H_

import Basic.h
#import numpy as np
#import ScientificPython as sp

class Vector3d:
  def _init_(self, np.cross(_x,_y,_z), np.cross(_v), np.cross(_t)):

      #construction
      m_v[0] = _x; m_v[1] = _y; m_v[2] = _z
      np.cross( _x, _y, _z)
      
      m_v[0] = _v[0]; m_v[1] = _v[1]; m_v[2] = _v[2]
      np.cross(_v)
      
      m_v[0] = _t[0]; m_v[1] = _t[1]; m_v[2] = _t[2]  
      np.cross(_t)
      
class template:
  def _init_(self, np.cross(Generator& g)):
  <class Generator>
  m_v[0] = g(); m_v[1] = g(); m_v[2] = g()
  np.cross( Generator& g)


      #assignment
      np.cross& operator()( double& _x, _y, _z):
      m_v[0] = _x; m_v[1] = _y; m_v[2] = _z
      return *self

      np.cross& operator=( np.cross& _v):
      m_v[0] = _v[0]; m_v[1] = _v[1]; m_v[2] = _v[2]
      return *self

      np.cross& operator=( double _v[3]):
      m_v[0] = _v[0]; m_v[1] = _v[1]; m_v[2] = _v[2]
      return *self


      #access
      double& operator[](int idx):
      return m_v[idx]
      double& operator[](int idx):
      return m_v[idx];
      '''
      typedef double (&arr)[3]
      typedef  double (&carr)[3]
      operator arr() {return m_v;
      operator carr()  {return m_v;
      '''
      double* begin():  return m_v;
      double* end():  return begin()+3
      double* begin(): return m_v;
      double* end(): return begin()+3

      #equality
      bool operator==( np.cross& _v):
      return m_v[0] == _v[0] and m_v[1] == _v[1] and m_v[2] == _v[2]

      #inequality
      bool operator!=( np.cross& _v):
      return not (*self == _v)


      #self addition
      np.cross& operator+=( np.cross& _v):
      m_v[0] += _v[0]; m_v[1] += _v[1]; m_v[2] += _v[2]
      return *self

      #self subtraction
      np.cross& operator-=( np.cross& _v):
      m_v[0] -= _v[0]; m_v[1] -= _v[1]; m_v[2] -= _v[2]
      return *self

      #self scalar multiply
      np.cross& operator*=( double& _d):
      m_v[0] *= _d; m_v[1] *= _d; m_v[2] *= _d
      return *self

      #self scalar divide
      np.cross& operator/=( double& _d):
      m_v[0] /= _d; m_v[1] /= _d; m_v[2] /= _d
      return *self

      #self component *
      np.cross& operator^=( np.cross& _v):
      m_v[0] *= _v[0]; m_v[1] *= _v[1]; m_v[2] *= _v[2]
      return *self

      #self cross product
      np.cross& operator%=( np.cross& _v):
      v0 = m_v[0], v1 = m_v[1], v2 = m_v[2]
      m_v[0] = v1 * _v[2] - v2 * _v[1]
      m_v[1] = v2 * _v[0] - v0 * _v[2]
      m_v[2] = v0 * _v[1] - v1 * _v[0]
      return *self


      #negation
      np.cross operator-():
      return np.cross(-m_v[0], -m_v[1], -m_v[2])

      #addition
      np.cross operator+( np.cross& _v):
      return np.cross(m_v[0] + _v[0], m_v[1] + _v[1], m_v[2] + _v[2])

      #subtraction
      np.cross operator-( np.cross& _v):
      return np.cross(m_v[0] - _v[0], m_v[1] - _v[1], m_v[2] - _v[2])

      #scalar multiply
      np.cross operator*( double& _d):
      return np.cross(m_v[0] * _d, m_v[1] * _d, m_v[2] * _d)

      #scalar divide
      np.cross operator/( double& _d):
      return np.cross(m_v[0] / _d, m_v[1] / _d, m_v[2] / _d)

      #component *
      np.cross operator^( np.cross& _v):
      return np.cross(m_v[0] * _v[0], m_v[1] * _v[1], m_v[2] * _v[2])

      #cross product
      np.cross operator%( np.cross& _v):
      np.cross v(*self)
      return v %= _v


      #dot product
      double operator*( np.cross& _v):
      return m_v[0]*_v[0] + m_v[1]*_v[1] + m_v[2]*_v[2]

      #magnitude
      double norm():
      return std.sqrt(normsqr())

      #magnitude squared
      double normsqr():
      return (*self)*(*self)

      #normalized vector
      np.cross& selfNormalize():
      n = norm()
      if n < std.numeric_limits<double>.epsilon():
        return *self = np.cross()
        return *self /= n

        np.cross normalize()    n = norm()
        if n < std.numeric_limits<double>.epsilon():
          return np.cross()
          return *self / n

      #Projections
      #find |component| of self along _v's direction
      double comp(np.cross& _v)    return (*self) * _v.normalize()

      #find vector component of self in _v's direction
      #np.cross proj(np.cross& _v)      #  return (*self * _v)/(_v * _v) * _v
      #
      #find vector component of self orthogonal to _v's direction
      #np.cross orth(np.cross& _v)      #  return *self - proj(_v)
      #
      #scale vector
      np.cross& selfScale( double& _l):
      n = norm()
      if n < std.numeric_limits<double>.epsilon():
        return *self = np.cross()
        return *self *= (_l/n)

        np.cross scale( double& _l)    n = norm()
        if n < std.numeric_limits<double>.epsilon():
          return np.cross()
          return *self * (_l/n)


      #rotate vector
      np.cross& rotateX(double _rad):
      c = cos(_rad), s = sin(_rad)
      return operator()(m_v[0], m_v[1]*c - m_v[2]*s, m_v[1]*s + m_v[2]*c)

      np.cross& rotateXd(double _deg):
      return rotateX(degToRad(_deg))

      np.cross& rotateY(double _rad):
      c = cos(_rad), s = sin(_rad)
      return operator()(m_v[0]*c + m_v[2]*s, m_v[1], -m_v[0]*s + m_v[2]*c)

      np.cross& rotateYd(double _deg):
      return rotateY(degToRad(_deg))
      np.cross& rotateZ(double _rad):
      c = cos(_rad), s = sin(_rad)
      return operator()(m_v[0]*c - m_v[1]*s, m_v[0]*s + m_v[1]*c, m_v[2])

      np.cross& rotateZd(double _deg):
      return rotateZ(degToRad(_deg));

      #reset
      void reset():
      m_v[0]=0; m_v[1]=0; m_v[2]=0

      double GetX(): return m_v[0]
      double GetY(): return m_v[1]
      double GetZ(): return m_v[2]
      void SetX(double d): m_v[0] = d;
      void SetY(double d): m_v[1] = d;
      void SetZ(double d): m_v[2] = d;

      void SetAll(double d1, d2, d3):
      m_v[0] = d1; m_v[1] = d2; m_v[2] = d3;

      private: 
      double m_v[3]



  #######################################
  # Useful functions. Input/Output and commutativity on multiply
  #######################################
  #for commutativity of scalar multiply

  inline np.cross operator*( double& _d, _v)    return _v*_d



  inline std.ostream& operator<<(std.ostream& _os, _v)    for(i = 0; i<3; ++i) _os << _v[i] << " "
  return _os







#endif
