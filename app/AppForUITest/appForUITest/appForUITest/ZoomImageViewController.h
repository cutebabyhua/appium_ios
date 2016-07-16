//
//  ZoomImageViewController.h
//  appForUITest
//
//  Created by hengjie chen on 29/6/2016.
//  Copyright © 2016 hengjie chen. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ZoomImageViewController : UIViewController <UIScrollViewDelegate>

@property (strong, nonatomic) IBOutlet UIScrollView *scrollView;
@property (strong, nonatomic) IBOutlet UIImageView *imageView;


@end
