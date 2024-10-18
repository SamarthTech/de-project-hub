/* eslint-disable react-hooks/exhaustive-deps */
'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Progress } from '@/components/ui/progress';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const sampleTexts = [
  "The quick brown fox jumps over the lazy dog.",
  "To be or not to be, that is the question.",
  "All that glitters is not gold.",
  "Where there's a will, there's a way.",
  "Actions speak louder than words.",
];

const TypingTest = () => {
  const [text, setText] = useState('');
  const [input, setInput] = useState('');
  const [timer, setTimer] = useState(60);
  const [isActive, setIsActive] = useState(false);
  const [wpm, setWpm] = useState(0);
  const [accuracy, setAccuracy] = useState(100);
  const [chartData, setChartData] = useState([]);
  const inputRef = useRef(null);

  useEffect(() => {
    let interval = null;
    if (isActive && timer > 0) {
      interval = setInterval(() => {
        setTimer((prevTimer) => prevTimer - 1);
        calculateStats();
      }, 1000);
    } else if (timer === 0) {
      clearInterval(interval);
      setIsActive(false);
      calculateFinalStats();
    }
    return () => clearInterval(interval);
  }, [isActive, timer]);

  const startTest = () => {
    setText(sampleTexts[Math.floor(Math.random() * sampleTexts.length)]);
    setInput('');
    setTimer(60);
    setIsActive(true);
    setWpm(0);
    setAccuracy(100);
    setChartData([]);
    inputRef.current.focus();
  };

  const calculateStats = () => {
    const words = input.trim().split(' ').length;
    const currentWpm = Math.round((words / (60 - timer)) * 60);
    setWpm(currentWpm);

    const accuracyPercentage = calculateAccuracy();
    setAccuracy(accuracyPercentage);

    setChartData((prevData) => [
      ...prevData,
      { time: 60 - timer, wpm: currentWpm, accuracy: accuracyPercentage },
    ]);
  };

  const calculateAccuracy = () => {
    const textWords = text.split(' ');
    const inputWords = input.trim().split(' ');
    let correctWords = 0;

    for (let i = 0; i < inputWords.length; i++) {
      if (inputWords[i] === textWords[i]) {
        correctWords++;
      }
    }

    return Math.round((correctWords / inputWords.length) * 100) || 100;
  };

  const calculateFinalStats = () => {
    const words = input.trim().split(' ').length;
    const finalWpm = Math.round((words / 1) * 60);
    setWpm(finalWpm);

    const finalAccuracy = calculateAccuracy();
    setAccuracy(finalAccuracy);
  };

  const handleInputChange = (e) => {
    if (!isActive && e.target.value.length === 1) {
      startTest();
    }
    setInput(e.target.value);
  };

  return (
    <div className="space-y-8">
      <Card>
        <CardHeader>
          <CardTitle>Typing Test</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="mb-4">
            <p className="text-lg font-medium mb-2">Type the following text:</p>
            <p className="bg-secondary p-4 rounded">{text}</p>
          </div>
          <Input
            ref={inputRef}
            value={input}
            onChange={handleInputChange}
            placeholder="Start typing here..."
            disabled={timer === 0}
            className="mb-4"
          />
          <div className="flex justify-between items-center mb-4">
            <p>Time remaining: {timer}s</p>
            <Button onClick={startTest}>
              {isActive ? 'Restart' : 'Start'}
            </Button>
          </div>
          <Progress value={(timer / 60) * 100} className="mb-4" />
          <div className="grid grid-cols-2 gap-4">
            <Card>
              <CardHeader>
                <CardTitle>WPM</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-4xl font-bold">{wpm}</p>
              </CardContent>
            </Card>
            <Card>
              <CardHeader>
                <CardTitle>Accuracy</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-4xl font-bold">{accuracy}%</p>
              </CardContent>
            </Card>
          </div>
        </CardContent>
      </Card>
      <Card>
        <CardHeader>
          <CardTitle>Performance Chart</CardTitle>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="time" label={{ value: 'Time (seconds)', position: 'insideBottom', offset: -5 }} />
              <YAxis yAxisId="left" label={{ value: 'WPM', angle: -90, position: 'insideLeft' }} />
              <YAxis yAxisId="right" orientation="right" label={{ value: 'Accuracy (%)', angle: 90, position: 'insideRight' }} />
              <Tooltip />
              <Legend />
              <Line yAxisId="left" type="monotone" dataKey="wpm" stroke="#8884d8" name="WPM" />
              <Line yAxisId="right" type="monotone" dataKey="accuracy" stroke="#82ca9d" name="Accuracy" />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  );
};

export default TypingTest;