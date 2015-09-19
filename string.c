#include <stdio.h>
#define IN 1
#define OUT 0
///* подсчет цифр, символов-разделителей и прочих символов */
size_t string(char **s);
int main(){

	char *str = NULL;
	size_t size = string(&str);
	printf("%s", str);

}
size_t string(char **s){
	char c;
	scanf("%c", &c);
	char *res = (char *)(malloc(1 * sizeof(char)));
	res[0] = c;
	size_t len = 1;
	while(c != '\n'){
		scanf("%c", &c);
		res = realloc(res, (len + 1) * sizeof(char));
		res[len] = c;
		++len;
	}
	res = realloc(res, (len + 1) * sizeof(char));
	res[len] = 0;
	*s = res;
	return len;
}

