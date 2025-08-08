'use client'

import { useState } from 'react'

interface TranslationResponse {
  translated_code: string
  source_language: string
  target_language: string
}

export default function Home() {
  const [inputCode, setInputCode] = useState('')
  const [outputCode, setOutputCode] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')
  const [translationDirection, setTranslationDirection] = useState<'vb-to-csharp' | 'csharp-to-vb'>('vb-to-csharp')

  const translateCode = async () => {
    if (!inputCode.trim()) {
      setError('Please enter some code to translate')
      return
    }

    setIsLoading(true)
    setError('')

    try {
      const sourceLanguage = translationDirection === 'vb-to-csharp' ? 'vb' : 'csharp'
      const targetLanguage = translationDirection === 'vb-to-csharp' ? 'csharp' : 'vb'

      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const response = await fetch(`${apiUrl}/translate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          code: inputCode,
          source_language: sourceLanguage,
          target_language: targetLanguage,
        }),
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Translation failed')
      }

      const data: TranslationResponse = await response.json()
      setOutputCode(data.translated_code)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred during translation')
    } finally {
      setIsLoading(false)
    }
  }

  const swapDirection = () => {
    setTranslationDirection(prev => prev === 'vb-to-csharp' ? 'csharp-to-vb' : 'vb-to-csharp')
    setInputCode(outputCode)
    setOutputCode('')
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            VB.NET ↔ C# Translator
          </h1>
          <p className="text-gray-600">
            Translate your code between VB.NET and C# using AI
          </p>
        </div>

        {/* Translation Direction Toggle */}
        <div className="flex justify-center mb-6">
          <div className="bg-white rounded-lg shadow-md p-1">
            <button
              onClick={() => setTranslationDirection('vb-to-csharp')}
              className={`px-6 py-2 rounded-md font-medium transition-colors ${
                translationDirection === 'vb-to-csharp'
                  ? 'bg-blue-500 text-white'
                  : 'text-gray-600 hover:text-gray-800'
              }`}
            >
              VB.NET → C#
            </button>
            <button
              onClick={() => setTranslationDirection('csharp-to-vb')}
              className={`px-6 py-2 rounded-md font-medium transition-colors ${
                translationDirection === 'csharp-to-vb'
                  ? 'bg-blue-500 text-white'
                  : 'text-gray-600 hover:text-gray-800'
              }`}
            >
              C# → VB.NET
            </button>
          </div>
        </div>

        {/* Main Content */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Input Section */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-gray-800">
                {translationDirection === 'vb-to-csharp' ? 'VB.NET Code' : 'C# Code'}
              </h2>
              <button
                onClick={swapDirection}
                className="text-blue-500 hover:text-blue-700 text-sm font-medium"
              >
                Swap
              </button>
            </div>
            <textarea
              value={inputCode}
              onChange={(e) => setInputCode(e.target.value)}
              placeholder={`Enter your ${translationDirection === 'vb-to-csharp' ? 'VB.NET' : 'C#'} code here...`}
              className="w-full h-80 p-4 border border-gray-300 rounded-lg resize-none focus:ring-2 focus:ring-blue-500 focus:border-transparent font-mono text-sm"
            />
            <button
              onClick={translateCode}
              disabled={isLoading || !inputCode.trim()}
              className="mt-4 w-full bg-blue-500 hover:bg-blue-600 disabled:bg-gray-300 text-white font-medium py-3 px-6 rounded-lg transition-colors"
            >
              {isLoading ? 'Translating...' : 'Translate'}
            </button>
          </div>

          {/* Output Section */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">
              {translationDirection === 'vb-to-csharp' ? 'C# Code' : 'VB.NET Code'}
            </h2>
            <textarea
              value={outputCode}
              readOnly
              placeholder="Translated code will appear here..."
              className="w-full h-80 p-4 border border-gray-300 rounded-lg resize-none bg-gray-50 font-mono text-sm"
            />
            {outputCode && (
              <button
                onClick={() => navigator.clipboard.writeText(outputCode)}
                className="mt-4 w-full bg-green-500 hover:bg-green-600 text-white font-medium py-3 px-6 rounded-lg transition-colors"
              >
                Copy to Clipboard
              </button>
            )}
          </div>
        </div>

        {/* Error Display */}
        {error && (
          <div className="mt-6 bg-red-50 border border-red-200 rounded-lg p-4">
            <p className="text-red-700">{error}</p>
          </div>
        )}

        {/* Loading Indicator */}
        {isLoading && (
          <div className="mt-6 text-center">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
            <p className="mt-2 text-gray-600">Translating your code...</p>
          </div>
        )}
      </div>
    </div>
  )
} 