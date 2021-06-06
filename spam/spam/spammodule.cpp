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
	if (!PyArg_ParseTuple(args, "s", &str)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL;
	
	const char* outmail = "sungzzuu@gmail.com";
	const char* outpw = "tjdwn*yunsj00";

	return Py_BuildValue("s", outpw);
}

static PyMethodDef SpamMethods[] = {
	{ "getSendInfo", spam_getSendInfo, METH_VARARGS,
	"Get sender Info." },
	{ NULL, NULL, 0, NULL } // 배열의 끝을 나타냅니다.
};

static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",            // 모듈 이름
	"It is test module.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
	-1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}
