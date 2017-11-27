package main

import (
	"fmt"
	"os"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
)

func main() {
	fmt.Println("main ...")
	if len(os.Args) < 2 {
		fmt.Println("you must specify a bucket")
		return
	}

	svc := s3.New(session.New(), &aws.Config{Region: aws.String("eu-west-1")})

	params := &s3.ListObjectsInput{
		//Bucket: aws.String("bucket-name"),
		Bucket: &os.Args[1],
	}

	resp, _ := svc.ListObjects(params)
	for _, key := range resp.Contents {
		fmt.Println(*key.Key)
	}
}
