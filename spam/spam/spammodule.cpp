#include "python.h" 
#include <string>
#include <fstream>

using namespace std;

static PyObject*



spam_getSendInfo(PyObject *self, PyObject *args)
{
	const char* str;
	int len = 0;
	string OutStr;
	if (!PyArg_ParseTuple(args, "s", &str)) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
		return NULL;
	
	const char* outmail = "sungzzuu@gmail.com";
	const char* outpw = "tjdwn*yunsj00";

	return Py_BuildValue("s", outpw);
}

static PyMethodDef SpamMethods[] = {
	{ "getSendInfo", spam_getSendInfo, METH_VARARGS,
	"Get sender Info." },
	{ NULL, NULL, 0, NULL } // �迭�� ���� ��Ÿ���ϴ�.
};

static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",            // ��� �̸�
	"It is test module.", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
	-1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}
