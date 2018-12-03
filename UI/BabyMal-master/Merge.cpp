#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <io.h>
#include <vector>
#include <fstream>
#include <iostream>

using namespace std;

struct tag_api
{
	char api_name[256];
	char dll_name[256];
	long long appearence;
	long long malware;
	struct tag_api *next;
};

void insert_api(tag_api **hp, tag_api *api)
{
	if (*hp == NULL)
	{
		*hp = api;
		return;
	}
	if (strcmp(api->api_name, (*hp)->api_name) < 0)
	{
		api->next = *hp;
		*hp = api;
		return;
	}
	tag_api *temp = *hp;
	while (temp->next != NULL)
	{
		if (strcmp(api->api_name, temp->next->api_name) < 0)
		{
			api->next = temp->next;
			temp->next = api;
			return;
		}
		temp = temp->next;
	}
	temp->next = api;
	return;
}

tag_api *load_apis(const char *api_file)
{
	FILE *fp = fopen(api_file, "r");
	if (fp == NULL)
		return NULL;
	tag_api *head = NULL;
	tag_api *temp = (tag_api *)malloc(sizeof(tag_api));
	while (fscanf(fp, "%s %s %lld %lld", temp->api_name, temp->dll_name, &(temp->appearence), &(temp->malware)) != EOF)
	{
		temp->next = NULL;
		insert_api(&head, temp);
		temp = (tag_api *)malloc(sizeof(tag_api));
	}
	free(temp);
	fclose(fp);
	return head;
}

tag_api *search_api(tag_api *head, const char *api_name, const char *dll_name)
{
	tag_api *temp = head;
	while (temp != NULL)
	{
		if (strcmp(api_name, temp->api_name) == 0 && strcmp(dll_name, temp->dll_name) == 0)
			return temp;
		temp = temp->next;
	}
	return NULL;
}

void add_apis(tag_api **hp, const char *out_file, bool malware)
{
	char buf[BUFSIZ];
	char *temp;
	char api_name[256], dll_name[256];
	tag_api *temp_api;
	FILE *fp = fopen(out_file, "r");
	while (fgets(buf, BUFSIZ, fp) != NULL)
	{
		temp = strstr(buf, "º¯ÊýÃû³Æ: ");
		if (temp != NULL)
		{
			memset(api_name, 0, 256);
			memset(dll_name, 0, 256);
			strncpy(api_name, temp + 10, strstr(buf, "(") - temp - 10);
			strncpy(dll_name, strstr(buf, "(") + 1, strstr(buf, ")") - strstr(buf, "(") - 1);
			temp_api = search_api(*hp, api_name, dll_name);
			if (temp_api == NULL)
			{
				temp_api = (tag_api *)malloc(sizeof(tag_api));
				strcpy(temp_api->api_name, api_name);
				strcpy(temp_api->dll_name, dll_name);
				temp_api->appearence = 0;
				temp_api->malware = 0;
				temp_api->next = NULL;
				insert_api(hp, temp_api);
			}
			temp_api->appearence++;
			if (malware)
				temp_api->malware++;
		}
	}
	fclose(fp);
	remove(out_file);
	return;
}

void write_apis(tag_api *head, const char *api_file)
{
	FILE *fp = fopen(api_file, "w");
	tag_api *temp = head;
	while (temp != NULL)
	{
		fprintf(fp, "%s %s %lld %lld\n", temp->api_name, temp->dll_name, temp->appearence, temp->malware);
		temp = temp->next;
	}
	fclose(fp);
}

void free_apis(tag_api *head)
{
	tag_api *temp = head;
	while (head != NULL)
	{
		temp = head;
		head = head->next;
		free(temp);
	}
	return;
}  

void GetAllFormatFiles(string path, vector<string>& files, string format)
{ 
	long   hFile = 0; 
	struct _finddata_t fileinfo;
	string p;
	if ((hFile = _findfirst(p.assign(path).append("\\*" + format).c_str(), &fileinfo)) != -1)
	{
		do
		{
			if ((fileinfo.attrib &  _A_SUBDIR))
			{
				if (strcmp(fileinfo.name, ".") != 0 && strcmp(fileinfo.name, "..") != 0)
				{
					//files.push_back(p.assign(path).append("\\").append(fileinfo.name) );  
					GetAllFormatFiles(p.assign(path).append("\\").append(fileinfo.name), files, format);
				}
			}
			else
			{
				files.push_back(p.assign(path).append("\\").append(fileinfo.name));
			}
		} while (_findnext(hFile, &fileinfo) == 0);

		_findclose(hFile);
	}
}

int main(int argc, char *argv[])
{
	string filePath = "softsnoop\\OutFiles\\";
	vector<string> files;
	string buffer;
	char* charBuffer = new char[256];

	string format = ".txt";
	GetAllFormatFiles(filePath, files, format);
	int size = files.size();
	
	for(int i = 0;i< size;i++)
	{
		buffer = files[i];
		strcpy(charBuffer, buffer.c_str());
		tag_api *head = load_apis("softsnoop\\OutFiles\\api.txt");
		add_apis(&head, charBuffer, true);
		write_apis(head, "softsnoop\\OutFiles\\api.txt");
		free_apis(head);
		printf("*******File Number Processed£º%d *******\n", (i + 1));
	}

	printf("Done!");
	system("pause");
	return 0;
}
