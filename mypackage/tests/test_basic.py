import pytest
import mypackage

def test_A():
    assert mypackage.subpackage_A.A.do_A()=="A"


def test_C():
    assert mypackage.submodule_C.do_C()=='c'
