require 'nn'
require 'paths'

print("hehe");

trainset = torch.load('cifar10-train.t7')
testset = torch.load('cifar10-test.t7')

classes = {'airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck'}

setmetatable(trainset,{__index=function(t,i)
      return {t.data[i],t.label[i]}
    end}
  );
  
trainset.data = trainset.data:double()

function trainset:size()
  return self.data:size(1)
end

mean = {}
stdv = {}

for i=1,3 do
  mean[i] = trainset.data[{{},{i},{},{}}]:mean()
  print('Channel '.. i ..',Mean: '..mean[i])
  trainset.data[{{},{i},{},{}}]:add(-mean[i])
  
  stdv[i] = trainset.data[{{},{i},{},{}}]:std()
  print('Channel '..i..',Standard Deviation: '..stdv[i])
  trainset.data[{{},{i},{},{}}]:div(stdv[i])
end

net = nn.Sequential()
net:add(nn.SpatialConvolution(3,6,5,5)) -- 3in,6out,5*5 convolutions kernel
net:add(nn.ReLU())
net:add(nn.SpatialMaxPooling(2,2,2,2))

net:add(nn.SpatialConvolution(6,16,5,5))
net:add(nn.ReLU())
net:add(nn.SpatialMaxPooling(2,2,2,2))
net:add(nn.View(16*5*5)) -- reshape from 3D into 1D

net:add(nn.Linear(16*5*5,120)) -- fully connected layer(input and weight matrix multiply)
net:add(nn.ReLU())
net:add(nn.Linear(120,84))
net:add(nn.ReLU())
net:add(nn.Linear(84,10)) -- 120 to 84 to 10

net:add(nn.LogSoftMax()) -- converts the output to a log-probability. useful for classification problems

criterion = nn.ClassNLLCriterion()
trainer = nn.StochasticGradient(net,criterion)
trainer.learningRate = 0.001
trainer.maxIteration = 5

trainer:train(trainset)

testset.data = testset.data:double()
for i=1,3 do
  testset.data[{{},{i},{},{}}]:add(-mean[i])
  testset.data[{{},{i},{},{}}]:div(stdv[i])
end

predicted = net:forward(testset.data[100])
print(classes[testset.label[100]])
print(predicted:exp())

for i=1,predicted:size(1) do
  print(classes[i],predicted[i])
end

correct = 0
for i=1,10000 do
  local groundtruth = testset.label[i]
  local prediction = net:forward(testset.data[i])
  local confidences,indices = torch.sort(prediction,true) -- descending order sort
  if groundtruth == indices[1] then
    correct = correct + 1
  end
end

print(correct,100*correct/10000 .. '% ')
class_preformance = {0,0,0,0,0,0,0,0,0,0}
for i = 1,10000 do
  local groundtruth = testset.label[i]
  local prediction = net:forward(testset.data[i])
  local confidences,indices = torch.sort(prediction,true)
  if groundtruth == indices[1] then
    class_preformance[groundtruth] = class_preformance[groundtruth] + 1
  end
end

for i=1,#classes do
  print(classes[i],100*class_preformance[i]/1000 .. ' %')
end





























