#include <stdio.h>
#include<iostream>
#include<algorithm>

#define MAX 2001

struct node{
    node * next;
    node * prev;
    int distance;
};

struct elem{
    int n, k;
};


int a[MAX];
int hlp_i=0;
int n, k;
int g[MAX];
node * graph[MAX][MAX];
node * prov[MAX];
node * vert,*q;
bool distance[MAX][MAX]; 
elem query[MAX*MAX];
int hlp_j=0;
node * nextt[MAX][MAX];
bool ia[MAX];
int ba[MAX];
bool iaa[MAX];
    
void bfs(int n,int k,int t){
    node * vert;
    vert=graph[n][k];
    while (vert!=NULL) {
        if (ba[vert->distance]!=t && !iaa[vert->distance]) {
            g[vert->distance]=g[n];
            ba[vert->distance]=t;
            bfs(vert->distance,k,t);
            if (!ia[vert->distance]) {
                a[hlp_i++]=vert->distance;           
                ia[vert->distance]=true;
            }
        }
        if (nextt[n][k]->prev!=NULL) {
            nextt[n][k]->prev->next=nextt[n][k]->next;
        } else {
            prov[n]=nextt[n][k]->next;
        }        
        vert=vert->next;
    }
	graph[n][k]=NULL;
    if (!ia[n]) {
        a[hlp_i++]=n;      
        ia[n]=true;
        
    }
}


int main(){
  std::cin >> n >> k;

    int i,j;
    for (i=0; i<n; i++)
        for (j=0; j<k; j++){
            graph[i][j]=NULL;
        }
    int ri, ra, rb;
    for (i=0; i<k; i++) {
        std::cin >> ri;
        for (j=0; j<ri; j++) {
            std::cin >> ra >> rb;
            ra--;
            rb--;

            vert=new node;			
            vert->distance=rb;
            vert->next=graph[ra][i];
            graph[ra][i]=vert;

            vert=new node;			
            vert->distance=ra;
            vert->next=graph[rb][i];
            graph[rb][i]=vert;
        }
    }

    for (i=0; i<n; i++) {             
        prov[i]=NULL;
        for (j=k-1; j>=0; j--) {
            if (graph[i][j]!=NULL) {
                vert=new node;
                vert->distance=j;
                vert->next=prov[i];
                if (prov[i]!=NULL) {
                    prov[i]->prev=vert;
                }
                vert->prev=NULL;
                prov[i]=vert;
                nextt[i][j]=vert;
            }           
        }
    }

    a[hlp_i++]=0;
    g[0]=1;
    int t=0;
	ia[0]=true;
	

    for (;hlp_i>0;) {      

        hlp_j=0;
        for (i=0; i<hlp_i; i++){
            iaa[a[i]] = true;
			      vert = prov[a[i]];
            while (vert != NULL) {
                q = graph[a[i]][vert->distance];
                while (q!=NULL) {
                    if (!distance[q->distance][vert->distance] && !ia[q->distance]) {
                        query[hlp_j].n=q->distance;   
                        query[hlp_j].k=vert->distance;
                        hlp_j++;
                        g[q->distance]= g[a[i]] + 1;
                        distance[q->distance][vert->distance]=true;
                    }                   
                    q=q->next;
                }
                vert=vert->next;
            }           
        }

        hlp_i = 0;
        for (i=0; i<hlp_j; i++) {            
            t++;
			      ba[query[i].n] = t;
            bfs(query[i].n, query[i].k, t);   
        }

        
    }
    
    if (g[n-1]>0) {
        std::cout << (g[n-1]-1) << "\n";
    } else {
        std::cout << "-1" << "\n";
    }

    return 0;
}